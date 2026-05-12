#!/bin/sh
# Apply remaining translations to the proc debug file
cd /Users/arthurbetter/hi3403-build/hi3403-docs/docs/multimedia/mpp

# Use sed to do all remaining replacements
# Note: This file must be executed with: sh /path/to/this/script
sed -i '' 's/VPSS通道输出分辨率指的是缩放模块的输出分辨率。/VPSS channel output resolution refers to the output resolution of the scaling module./g' "13-proc调试信息-1316-1329.en.md"
sed -i '' 's/VPSS LDCI的proc信息（vpss ldci attr）仅SS524V100\/SS522V100支持。开启LDCI功能时才会显示具体的属性值，否则只显示属性字段。/VPSS LDCI proc info (vpss ldci attr) is only supported by SS524V100\/SS522V100. Specific attribute values are displayed only when the LDCI function is enabled; otherwise, only attribute fields are shown./g' "13-proc调试信息-1316-1329.en.md"
sed -i '' 's/SS524V100\/SS522V100\/SS928V100的VPSS IP个数是1，vpss hardware node queue和vpss int work status中只有VPSS0相关的信息。/SS524V100\/SS522V100\/SS928V100 have 1 VPSS IP. vpss hardware node queue and vpss int work status only contain VPSS0-related info./g' "13-proc调试信息-1316-1329.en.md"
sed -i '' 's/SS528V100\/SS625V100\/SS524V100\/SS522V100\/SS928V100\/SS626V100无Proc队列，Proc队列的节点数是0。/SS528V100\/SS625V100\/SS524V100\/SS522V100\/SS928V100\/SS626V100 have no Proc queue. Proc queue node count is 0./g' "13-proc调试信息-1316-1329.en.md"
echo "Done with batch 1"
