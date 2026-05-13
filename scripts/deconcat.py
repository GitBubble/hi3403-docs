"""Post-processing pass: split concatenated English words produced by CJK removal.

When CJK characters are removed from mixed CJK/English text, the remaining
English words are concatenated without spaces (e.g., "RegardingVPSSto").
This module splits them back apart using English word frequency data.

Also handles cases like "Compareexample" where a word boundary was lost.
"""

import re

# Common English words (top ~1000 by frequency) — used for dictionary-based splitting
COMMON_WORDS: set[str] = None  # lazy-loaded

# Known technical acronyms that should NOT be split
TECH_ACRONYMS = {
    'VPSS', 'VGS', 'VDP', 'VO', 'VI', 'VENC', 'VDEC', 'GDC', 'FRC', 'DCI',
    'LDCI', 'LTI', 'CTI', 'DEI', 'IE', 'NR', '3DNR', 'WBC', 'VHD', 'DSD',
    'DHD', 'UHD', 'HD', 'SD', 'WD', 'MPP', 'SDK', 'API', 'CPU', 'GPU',
    'DDR', 'SDRAM', 'MMZ', 'VQE', 'AI', 'AENC', 'ADEC', 'AO', 'AI',
    'LCU', 'MB', 'GOP', 'QP', 'QPMAP', 'ROI', 'HDR', 'LDC', 'VGS',
    'MDC', 'ARM', 'PCIe', 'USB', 'SDIO', 'SPI', 'I2C', 'UART', 'GPIO',
    'PWM', 'IR', 'HDMI', 'MIPI', 'LVDS', 'BT', 'SLVDS', 'CMOS',
}

# Patterns that should NOT be split (keep original)
PRESERVE_PATTERNS = re.compile(
    r'(?:^|_)'  # start of string or underscore
    r'[A-Z][A-Z0-9_]{2,}'  # all-caps acronyms with digits
    r'(?:$|_)'  # end of string or underscore
)

# The core pattern: lowercase letter immediately before uppercase letter
# that starts a lowercase sequence (i.e., a new word)
CONCAT_SPLIT = re.compile(r'([a-z])([A-Z][a-z])')


def load_word_list():
    """Load common English words."""
    global COMMON_WORDS
    if COMMON_WORDS is not None:
        return COMMON_WORDS

    COMMON_WORDS = set()
    # Try system dictionary
    for dict_path in ['/usr/share/dict/words', '/usr/dict/words']:
        try:
            with open(dict_path) as f:
                for line in f:
                    word = line.strip().lower()
                    if len(word) >= 2 and word.isalpha():
                        COMMON_WORDS.add(word)
            break
        except FileNotFoundError:
            continue

    # If no system dict, use a built-in set of common tech-doc words
    if not COMMON_WORDS:
        COMMON_WORDS = _builtin_words()

    # Add common technical terms
    COMMON_WORDS.update({
        'buffer', 'channel', 'display', 'video', 'audio', 'image', 'frame',
        'resolution', 'memory', 'mode', 'format', 'output', 'input', 'control',
        'sync', 'layer', 'device', 'writeback', 'region', 'rotation', 'scaling',
        'zoom', 'crop', 'cover', 'overlay', 'mosaic', 'border', 'aspect',
        'pixel', 'bitrate', 'bitstream', 'encoder', 'decoder', 'splicing',
        'deinterlace', 'denoise', 'enhance', 'correct', 'distortion',
        'parameter', 'attribute', 'member', 'structure', 'interface',
        'handle', 'pointer', 'callback', 'thread', 'process', 'module',
        'pipeline', 'offline', 'online', 'bypass', 'bind', 'unbind',
        'allocate', 'release', 'enable', 'disable', 'configure', 'register',
        'interrupt', 'timeout', 'capture', 'render', 'convert', 'compress',
        'decompress', 'encode', 'decode', 'sample', 'filter', 'detect',
        'ratio', 'width', 'height', 'size', 'coordinate', 'position',
        'timestamp', 'delay', 'latency', 'frequency', 'clock', 'timing',
        'current', 'previous', 'next', 'maximum', 'minimum', 'average',
        'positive', 'negative', 'horizontal', 'vertical', 'progressive',
        'interlaced', 'gathered', 'scattered', 'physical', 'virtual',
        'dynamic', 'static', 'normal', 'special', 'default', 'custom',
        'valid', 'invalid', 'supported', 'unsupported', 'reserved',
        'required', 'optional', 'recommended', 'deprecated',
        'rate', 'line', 'field', 'block', 'macroblock', 'slice',
        'chroma', 'luma', 'luminance', 'saturation', 'contrast', 'hue',
        'gamma', 'white', 'balance', 'exposure', 'focus', 'stabilization',
        'fisheye', 'corridor', 'privacy', 'motion', 'tampering', 'diagnostics',
        'intelligent', 'analysis', 'detection', 'recognition', 'synthesis',
        'echo', 'cancellation', 'enhancement', 'localization',
    })

    return COMMON_WORDS


def _builtin_words():
    """Fallback word set from common English words."""
    return {
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'then', 'else', 'when',
        'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
        'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might',
        'can', 'shall', 'must', 'need', 'dare', 'ought', 'used', 'to',
        'of', 'in', 'on', 'at', 'by', 'for', 'with', 'about', 'against',
        'between', 'through', 'during', 'before', 'after', 'above', 'below',
        'from', 'up', 'down', 'out', 'off', 'over', 'under', 'again', 'further',
        'then', 'once', 'here', 'there', 'where', 'when', 'why', 'how', 'all',
        'each', 'every', 'both', 'few', 'more', 'most', 'other', 'some', 'such',
        'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just', 'because',
        'as', 'until', 'while', 'not', 'no', 'nor', 'this', 'that', 'these',
        'those', 'which', 'who', 'whom', 'whose', 'what', 'it', 'its', 'he',
        'she', 'they', 'them', 'their', 'we', 'us', 'our', 'you', 'your',
        'one', 'two', 'three', 'any', 'first', 'last', 'next', 'new', 'old',
        'high', 'low', 'large', 'small', 'long', 'short', 'full', 'half',
        'single', 'multiple', 'many', 'several', 'less', 'least', 'much',
        'data', 'set', 'get', 'put', 'add', 'use', 'make', 'take', 'see',
        'know', 'think', 'say', 'come', 'go', 'look', 'want', 'give', 'find',
        'tell', 'ask', 'try', 'leave', 'call', 'keep', 'let', 'begin', 'seem',
        'help', 'show', 'hear', 'play', 'run', 'move', 'live', 'believe',
        'hold', 'bring', 'happen', 'write', 'provide', 'sit', 'stand', 'lose',
        'pay', 'meet', 'include', 'continue', 'change', 'lead', 'understand',
        'watch', 'follow', 'stop', 'create', 'speak', 'read', 'allow', 'order',
        'spend', 'grow', 'open', 'walk', 'win', 'offer', 'remember', 'love',
        'consider', 'appear', 'buy', 'wait', 'serve', 'die', 'send', 'expect',
        'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'remain', 'suggest',
        'raise', 'pass', 'sell', 'require', 'report', 'decide', 'pull',
    }


def segment_word(run):
    """Segment a concatenated English run into words using dictionary.

    Uses greedy longest-match segmentation.
    Returns segmented string or original if segmentation fails.
    """
    words = load_word_list()
    original = run
    run_lower = run.lower()

    # Try greedy segmentation
    result = []
    pos = 0
    last_split = 0
    while pos < len(run):
        best_len = 0
        # Try to match the longest word starting at pos
        for end in range(min(pos + 20, len(run)), pos + 1, -1):
            if run_lower[pos:end] in words:
                best_len = end - pos
                break

        if best_len >= 2:
            if pos > last_split:
                result.append(run[last_split:pos])  # unmatched fragment
            result.append(run[pos:pos + best_len])
            pos = pos + best_len
            last_split = pos
        else:
            pos += 1

    if last_split < len(run):
        result.append(run[last_split:])

    # Only return segmented version if it's different and has enough splits
    if len(result) > 1:
        return ' '.join(result)
    return original


# Also split lowercase before all-caps acronym: InitializationMPP → Initialization MPP
# Non-greedy: only capture uppercase run that is NOT followed by a lowercase letter
# (otherwise it's CamelCase and handled above)
ACRONYM_SPLIT = re.compile(r'([a-z])([A-Z]{2,})')

# Split acronym-then-CamelCase: VPSSChannel → VPSS Channel, MMZModule → MMZ Module
ACRONYM_CAMEL_SPLIT = re.compile(r'([A-Z])([A-Z][a-z])')


def _has_underscore_nearby(text, pos, radius=30):
    """Check if there's an underscore near the given position."""
    start = max(0, pos - radius)
    end = min(len(text), pos + radius)
    return '_' in text[start:end]


def deconcat_text(text: str) -> str:
    """Split concatenated English words in text.

    Handles patterns like:
    - RegardingVPSSto → Regarding VPSS to
    - UserUsesThisInterface → User Uses This Interface
    - InitializationMPP → Initialization MPP

    Does NOT split API identifiers (strings containing underscores within 30 chars).
    """
    original = text

    def near_underscore(m):
        """Check if match is within 30 chars of an underscore."""
        lo = max(0, m.start() - 30)
        hi = min(len(original), m.end() + 30)
        return '_' in original[lo:hi]

    def split_camel(m):
        if near_underscore(m):
            return m.group(0)
        return m.group(1) + ' ' + m.group(2)

    def split_acronym(m):
        if near_underscore(m):
            return m.group(0)
        # Don't split if the acronym is followed by lowercase (it's CamelCase, handled above)
        next_pos = m.end()
        if next_pos < len(original) and original[next_pos].islower():
            return m.group(0)
        return m.group(1) + ' ' + m.group(2)

    for _ in range(3):
        new_text = CONCAT_SPLIT.sub(split_camel, text)
        if new_text == text:
            break
        text = new_text

    for _ in range(2):
        new_text = ACRONYM_SPLIT.sub(split_acronym, text)
        if new_text == text:
            break
        text = new_text

    # Step 3: split acronym-then-CamelCase
    def split_acronym_camel(m):
        if near_underscore(m):
            return m.group(0)
        return m.group(1) + ' ' + m.group(2)

    for _ in range(2):
        new_text = ACRONYM_CAMEL_SPLIT.sub(split_acronym_camel, text)
        if new_text == text:
            break
        text = new_text

    return text


# Interface compatible with phrases.py passes
DECONCAT_PASS = [('__DECONCAT__', '__DECONCAT__')]  # marker, handled specially


def apply_deconcat(text: str) -> str:
    """Apply deconcatenation to text. Called as a special pass."""
    return deconcat_text(text)
