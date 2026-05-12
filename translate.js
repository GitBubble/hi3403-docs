// Node.js script to translate Chinese proc documentation to English
const fs = require('fs');
const path = require('path');

const inputFile = '/Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/mpp/13-proc调试信息-1316-1329.md';
const outputFile = '/Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/mpp/13-proc调试信息-1316-1329.en.md';

// Translation dictionary
const translations = {
    '【调试信息】': '[Debug Info]',
    '【调试信息分析】': '[Debug Info Analysis]',
    '【参数说明】': '[Parameter Description]',
    '【调试信息说明】': '[Debug Info Description]',
    '参数': 'Parameter',
    '描述': 'Description',
    'Grp ID号。': 'Grp ID number.',
    '有效范围：': 'Valid range: ',
    '单位：像素': 'Unit: pixel',
    '以像素为单位': 'in pixels',
    '使能。': 'Enable.',
    '使能：': 'Enable: ',
    '使能状态': 'Enable status',
    '是否使能': 'Whether to enable',
    'Y：使能；': 'Y: Enable;',
    'N：不使能。': 'N: Disable.',
    'Y：使能。': 'Y: Enable.',
    'N：不使能；': 'N: Disable;',
    'Y：打开；': 'Y: On;',
    'Y：打开。': 'Y: On.',
    'N：关闭；': 'N: Off;',
    'N：关闭。': 'N: Off.',
    '0：不使能；': '0: Disable;',
    '1：使能。': '1: Enable.',
    '0：不使用；': '0: Not used;',
    '1：使用。': '1: Used.',
    '0：静音数据；': '0: Mute data;',
    '1：非静音数据。': '1: Non-mute data.',
    'NULL：未占用；': 'NULL: Not occupied;',
    '1：占用。': '1: Occupied.',
    '坐标类型。': 'Coordinate type.',
    'RAT：相对坐标；': 'RAT: Relative coordinate;',
    'ABS：绝对坐标。': 'ABS: Absolute coordinate.',
    'N：使能。': 'N: Enable.',
    'Y：不使能。': 'Y: Disable.',
    'N：使能；': 'N: Enable;',
    'N：不使能': 'N: Disable',
    'Y：使能': 'Y: Enable',
    'Y：支持。': 'Y: Supported.',
    'N：不支持。': 'N: Not supported.',
    'Y：支持': 'Y: Supported',
    'N：不支持': 'N: Not supported',
    'Y：压缩；': 'Y: Compressed;',
    'N：非压缩。': 'N: Uncompressed.',
    'Y：开启；': 'Y: On;',
    'Y：开启。': 'Y: On.',
    'Y：静音打开；': 'Y: Mute on;',
    'N：静音关闭。': 'N: Mute off.',
    'N：自动模式；': 'N: Auto mode;',
    'Y：用户模式。': 'Y: User mode.',
    'Y：启用重采样功能；': 'Y: Resampling enabled;',
    'N：关闭重采样功能。': 'N: Resampling disabled.',
    'Y：启用声音质量增强功能；': 'Y: Voice quality enhancement enabled;',
    'N：关闭声音质量增强功能。': 'N: Voice quality enhancement disabled.',
    'Y：启用自动增益控制功能；': 'Y: AGC enabled;',
    'N：关闭自动增益控制功能。': 'N: AGC disabled.',
    'Y：启用均衡器功能；': 'Y: EQ enabled;',
    'N：关闭均衡器功能。': 'N: EQ disabled.',
    'Y：启用向文件存储通道数据功能；': 'Y: File storage enabled;',
    'N：关闭向文件存储通道数据功能。': 'N: File storage disabled.',
    'N：关闭': 'N: Off',
    'Y：打开': 'Y: On',
    'N：关闭；': 'N: Off;',
    '0：IP0': '0: IP0',
    '1：IP1': '1: IP1',
    '2：IP2': '2: IP2',
    'NONE：非压缩；': 'NONE: Uncompressed;',
    'SEG：非紧凑段压缩；': 'SEG: Non-compact segment compression;',
    'SEG_COMPACT：紧凑段压缩；': 'SEG_COMPACT: Compact segment compression;',
    'TILE：Tile压缩。': 'TILE: Tile compression.',
    'LINE：行压缩。': 'LINE: Line compression.',
    'NONE：关闭幅形比': 'NONE: Aspect ratio off',
    'AUTO：自动模式': 'AUTO: Auto mode',
    'MANUAL：手动模式': 'MANUAL: Manual mode',
    'OFF：强制关闭；': 'OFF: Force off;',
    'ON：强制打开；': 'ON: Force on;',
    'AUTO：自适应。': 'AUTO: Adaptive.',
    'VER_1：版本1；': 'VER_1: Version 1;',
    'VER_2：版本2。': 'VER_2: Version 2.',
    'NORMAL：正常调度模式。': 'NORMAL: Normal scheduling mode.',
    'QUICK：快速调度模式。': 'QUICK: Quick scheduling mode.',
    'VIDEO：视频模式；': 'VIDEO: Video mode;',
    'SNAP：拍照模式。': 'SNAP: Snapshot mode.',
    'VIDEO_SPA：视频纯空域模式。': 'VIDEO_SPA: Video pure spatial mode.',
    'NORM：普通模式；': 'NORM: Normal mode;',
    'COMPENSATION：运动补偿模式。': 'COMPENSATION: Motion compensation mode.',
    'USER：USER模式；': 'USER: USER mode;',
    'AUTO：AUTO模式。': 'AUTO: AUTO mode.',
    'NORMAL：通过sys接口配置的缩放系数。': 'NORMAL: Scaling factor configured through sys interface.',
    'BILINEAR：双线性缩放系数。': 'BILINEAR: Bilinear scaling factor.',
    'FREE：任意角度旋转': 'FREE: Arbitrary angle rotation',
    'FREE_HP：高精度任意角度旋转': 'FREE_HP: High precision arbitrary angle rotation',
    'ALL：全模式；': 'ALL: Full mode;',
    'TYPICAL：经典模式；': 'TYPICAL: Classic mode;',
    'INSIDE：无黑边模式。': 'INSIDE: No black border mode.',
    'START：帧起始中断；': 'START: Frame start interrupt;',
    'EARLY：帧起始延时中断；': 'EARLY: Frame start delayed interrupt;',
    'EARLY_END：帧起始延时中断和帧完成中断。': 'EARLY_END: Frame start delayed interrupt and frame completion interrupt.',
    'orig：初始状态；': 'orig: Initial state;',
    'enable：启用；': 'enable: Enabled;',
    'disable：禁用。': 'disable: Disabled.',
    'normal：正常模式；': 'normal: Normal mode;',
    'fast：快速模式。': 'fast: Fast mode.',
    'comm：一般模式；': 'comm: Communication mode;',
    'music：音乐模式；': 'music: Music mode;',
    'noisy：噪声模式。': 'noisy: Noisy mode.',
    'mono：单声道；': 'mono: Mono;',
    'stereo：立体声。': 'stereo: Stereo.',
    'rise：上升沿；': 'rise: Rising edge;',
    'fall：下降沿。': 'fall: Falling edge.',
    'y：启用；': 'y: Enabled;',
    'n：未启用。': 'n: Not enabled.',
    'n：未启用。': 'n: Not enabled.',
    'LIMITED：YUV图像量化范围是[16, 235]。': 'LIMITED: YUV image quantization range is [16, 235].',
    'FULL：YUV图像量化范围是[0, 255]。': 'FULL: YUV image quantization range is [0, 255].',
    'MOD：模块VB；': 'MOD: Module VB;',
    'PRIVATE：私有VB；': 'PRIVATE: Private VB;',
    'USER：用户VB。': 'USER: User VB.',
    'i2s_mas：I2S主模式。': 'i2s_mas: I2S master mode.',
    'i2s_sla：I2S从模式。': 'i2s_sla: I2S slave mode.',
    'pcm0_mt：标准PCM主模式。': 'pcm0_mt: Standard PCM master mode.',
    'pcm0_sl：标准PCM从模式。': 'pcm0_sl: Standard PCM slave mode.',
    'pcm1_mt：非标准PCM主模式。': 'pcm1_mt: Non-standard PCM master mode.',
    'pcm1_sl：非标准PCM从模式。': 'pcm1_sl: Non-standard PCM slave mode.',
};

function translateText(text) {
    if (!text) return text;

    // Sort keys by length (longest first) to avoid partial replacements
    const sortedKeys = Object.keys(translations).sort((a, b) => b.length - a.length);

    let result = text;
    for (const key of sortedKeys) {
        if (result.includes(key)) {
            result = result.split(key).join(translations[key]);
        }
    }
    return result;
}

// Read file
const content = fs.readFileSync(inputFile, 'utf-8');
const lines = content.split('\n');

let inCodeBlock = false;
const outputLines = [];

for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    // Track code blocks
    if (trimmed.startsWith('```')) {
        inCodeBlock = !inCodeBlock;
        outputLines.push(line);
        continue;
    }

    // In code blocks, preserve content exactly
    if (inCodeBlock) {
        outputLines.push(line);
        continue;
    }

    // Translate line
    outputLines.push(translateText(line));
}

// Write output
fs.writeFileSync(outputFile, outputLines.join('\n'), 'utf-8');
console.log('Translation complete. Output written to ' + outputFile);
