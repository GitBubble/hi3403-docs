---
description: Compare several Hi3403 development boards supported by the Hi3403 platform and choose the one that suits you
title: Choose a development board
--- # Choose a development board The Hi3403 platform currently has these mainstream Hi3403V100 development boards. Each board has different choices
——Price, peripherals, document completeness, and community ecology. The table below gives you a quick comparison, below
Decision tree helps you choose in 30 seconds. ## Quick comparison | Board | Vendor | price | peripherals | Document | Suitable for whom |
|---|---|---|---|---|---|
| [iTOP-Hi3403](../boards/topeet/index.md) | Topeet | middle | richest | The most complete | **Getting Started, SDK Development** |
| [LubanCat-Hi3403](../boards/lubancat/index.md) | wildfire | middle | medium | Complete (Buildroot friendly) | Buildroot user, custom system |
| [Euler Pi](../boards/ebaina/index.md) | Ebaina | middle | medium | OpenEuler is well adapted | OpenEuler Developer |
| [Run Kaihong](../boards/rkh/index.md) | Run Kaihong | — | — | OpenHarmony Desktop Adaptation | OpenHarmony device development |
| [Zhongshan Kuangshi (zsks)](../boards/zsks/index.md) | Zhongshan Kuangshi | — | Contains rich AI demos | Partial AI Example | Get started with a ready-made AI demo | !!! note "Hardware features are based on Hi3403V100 SoC" The *core* capabilities (NPU, ISP, codec, memory bandwidth) of all boards come from the same chip
SoC. The differences are mainly in peripheral layout, power supply design, attached sensor/camera module,
SDK images and documentation provided by the manufacturer. ## 30 second decision tree ```mermaid
flowchart TD Start[What am I going to do?] --> A{First time with Hi3403?} A -- Yes --> Topeet[iTOP-Hi3403<br> complete peripherals + complete documentation] A -- No --> B{What type of system?} B -- OpenHarmony device --> RKH[Run Kaihong] B -- OpenEuler --> Ebaina[Euler Pi] B -- Buildroot --> LubanCat[LubanCat-Hi3403] B -- AI application demo --> ZSKS[Zhongshan Kuangshi zsks] B -- Ubuntu desktop --> Topeet style Topeet stroke:#7c4dff,stroke-width:3px style LubanCat stroke:#7c4dff,stroke-width:2px style Ebaina stroke:#7c4dff,stroke-width:2px style RKH stroke:#7c4dff,stroke-width:2px style ZSKS stroke:#7c4dff,stroke-width:2px
``` ## Detailed comparison items ### Recommended scenarios - **Newbie/Learning SDK** → iTOP-Hi3403. SDK default target board, with the most community information,
You have the highest probability of finding the answer by digging into the pits.
- **Volume Production Engineering/Customized Linux** → LubanCat-Hi3403. The Buildroot project link is mature.
- **OpenHarmony App** → RKH. Desktop system adaptation is the best.
- **OpenEuler localization** → Euler Pi.
- **AI algorithm verification** → Zhongshan Kuangshi. The demo provided can be run directly (face_detection,
kcf_track, fruit_identify, opencv_dnn, hnr_auto), suitable for seeing the effect without writing code. ### None? If you already have other Hi3403V100 self-developed boards (such as Hi3403V100 reference design),
You can also use this set of documents - Hi3403 SDK and the multimedia/AI documents here are at the chip level.
It has nothing to do with the specific board. Please refer to the board-specific content (pinout, schematic diagram, Flashing script)
Information provided by your board manufacturer. ## Next <div class="grid cards" markdown> - :material-clock-fast:{ .lg .middle } __Selected, I want to light it__ --- [:octicons-arrow-right-24: Boot Hi3403 in 30 minutes](quickstart.md) - :material-disc-player:{ .lg .middle } __Selected, but still struggling with the operating system__ --- [:octicons-arrow-right-24: Select operating system](os-picker.md) - :material-developer-board:{ .lg .middle } __View detailed information of each board__ --- [:octicons-arrow-right-24: development board](../boards/index.md) </div>