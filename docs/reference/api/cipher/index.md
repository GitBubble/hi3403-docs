---
title: "前言"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/CIPHER API 参考/CIPHER API 参考.md
---

# 前言
**概述<a name="section5005mcpsimp"></a>**

CIPHER是安全算法模块，它提供了AES对称加解密算法，HASH及HMAC摘要算法，随机数算法，以及RSA不对称算法，主要用于对音视频码流进行加解密及数据合法性验证等场景。

>![](public_sys-resources/icon-note.gif) **说明：** 
>本文未有特殊说明，SS927V100与SS928V100内容完全一致。

**产品版本<a name="section5008mcpsimp"></a>**

与本文档相对应的产品版本如下。

<a name="table5011mcpsimp"></a>
<table><thead align="left"><tr id="row5016mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p5018mcpsimp"><a name="p5018mcpsimp"></a><a name="p5018mcpsimp"></a>产品名称</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p5020mcpsimp"><a name="p5020mcpsimp"></a><a name="p5020mcpsimp"></a>产品版本</p>
</th>
</tr>
</thead>
<tbody><tr id="row5022mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p5024mcpsimp"><a name="p5024mcpsimp"></a><a name="p5024mcpsimp"></a>SS928</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p5026mcpsimp"><a name="p5026mcpsimp"></a><a name="p5026mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row5027mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p5029mcpsimp"><a name="p5029mcpsimp"></a><a name="p5029mcpsimp"></a>SS626</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p5031mcpsimp"><a name="p5031mcpsimp"></a><a name="p5031mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row10245112718406"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>SS927</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**读者对象<a name="section5032mcpsimp"></a>**

本文档（本指南）主要适用于以下工程师：

-   技术支持工程师
-   软件开发工程师

**符号约定<a name="section5038mcpsimp"></a>**

在本文中可能出现下列标志，它们所代表的含义如下。

<a name="table5041mcpsimp"></a>
<table><thead align="left"><tr id="row5046mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.3.1.1"><p id="p5048mcpsimp"><a name="p5048mcpsimp"></a><a name="p5048mcpsimp"></a>符号</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.1.3.1.2"><p id="p5050mcpsimp"><a name="p5050mcpsimp"></a><a name="p5050mcpsimp"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row5052mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p5054mcpsimp"><a name="p5054mcpsimp"></a><a name="p5054mcpsimp"></a><a name="image216"></a><a name="image216"></a><span><img id="image216" src="figures/zh-cn_image_0000002441653093.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p5056mcpsimp"><a name="p5056mcpsimp"></a><a name="p5056mcpsimp"></a>表示如不避免则将会导致死亡或严重伤害的具有高等级风险的危害。</p>
</td>
</tr>
<tr id="row5057mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p5059mcpsimp"><a name="p5059mcpsimp"></a><a name="p5059mcpsimp"></a><a name="image217"></a><a name="image217"></a><span><img id="image217" src="figures/zh-cn_image_0000002408093786.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p5061mcpsimp"><a name="p5061mcpsimp"></a><a name="p5061mcpsimp"></a>表示如不避免则可能导致死亡或严重伤害的具有中等级风险的危害。</p>
</td>
</tr>
<tr id="row5062mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p5064mcpsimp"><a name="p5064mcpsimp"></a><a name="p5064mcpsimp"></a><a name="image218"></a><a name="image218"></a><span><img id="image218" src="figures/zh-cn_image_0000002408253682.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p5066mcpsimp"><a name="p5066mcpsimp"></a><a name="p5066mcpsimp"></a>表示如不避免则可能导致轻微或中度伤害的具有低等级风险的危害。</p>
</td>
</tr>
<tr id="row5067mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p5069mcpsimp"><a name="p5069mcpsimp"></a><a name="p5069mcpsimp"></a><a name="image219"></a><a name="image219"></a><span><img id="image219" src="figures/zh-cn_image_0000002441572941.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p5071mcpsimp"><a name="p5071mcpsimp"></a><a name="p5071mcpsimp"></a>用于传递设备或环境安全警示信息。如不避免则可能会导致设备损坏、数据丢失、设备性能降低或其它不可预知的结果。</p>
<p id="p5072mcpsimp"><a name="p5072mcpsimp"></a><a name="p5072mcpsimp"></a>“须知”不涉及人身伤害。</p>
</td>
</tr>
<tr id="row5073mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p5075mcpsimp"><a name="p5075mcpsimp"></a><a name="p5075mcpsimp"></a><a name="image220"></a><a name="image220"></a><span><img id="image220" src="figures/zh-cn_image_0000002441572945.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p5077mcpsimp"><a name="p5077mcpsimp"></a><a name="p5077mcpsimp"></a>对正文中重点信息的补充说明。</p>
<p id="p5078mcpsimp"><a name="p5078mcpsimp"></a><a name="p5078mcpsimp"></a>“说明”不是安全警示信息，不涉及人身、设备及环境伤害信息。</p>
</td>
</tr>
</tbody>
</table>

**修订记录<a name="section5079mcpsimp"></a>**

修订记录累积了每次文档更新的说明。最新版本的文档包含以前所有文档版本的更新内容。

<a name="table2161mcpsimp"></a>
<table><thead align="left"><tr id="row2167mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p2169mcpsimp"><a name="p2169mcpsimp"></a><a name="p2169mcpsimp"></a>文档版本</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="p2171mcpsimp"><a name="p2171mcpsimp"></a><a name="p2171mcpsimp"></a>发布日期</p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p2173mcpsimp"><a name="p2173mcpsimp"></a><a name="p2173mcpsimp"></a>修改说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row2175mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p2177mcpsimp"><a name="p2177mcpsimp"></a><a name="p2177mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p2179mcpsimp"><a name="p2179mcpsimp"></a><a name="p2179mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p2181mcpsimp"><a name="p2181mcpsimp"></a><a name="p2181mcpsimp"></a>第1次临时版本发布。</p>
</td>
</tr>
</tbody>
</table>

# 概述
## 概述<a name="ZH-CN_TOPIC_0000002408093758"></a>

CIPHER是安全算法模块，其提供了包括AES对称加解密算法，RSA不对称加解密算法，随机数生成，以及支持HASH、HMAC等摘要算法，主要用于对音视频码流进行加解密保护，用户合法性认证等场景。各功能划分如下。








### 对称加解密算法<a name="ZH-CN_TOPIC_0000002408093762"></a>

-   AES：支持ECB/CBC/CFB/OFB/CTR/CCM/GCM等工作模式。CCM/GCM模式下，加解密结束后需获取一次TAG值。
-   以上算法除了CTR/CCM/GCM，其它算法、模式的数据长度必须按块大小对齐；CCM/GCM的N、A需要靠软件按标准把各个字段封装成块大小对齐的数据块；各种工作模式支持一次实现多个分组的加解密运算，也支持一次实现单个分组的加解密运算。
-   SS928V100、SS626V100支持申请15个通道。
-   ECB模式安全性低，该模式仅用于调试，不能用于产品。

### 不对称加解密算法<a name="ZH-CN_TOPIC_0000002441572925"></a>

RSA：支持密钥位宽2048/3072/4096 bits。

### 随机数生成<a name="ZH-CN_TOPIC_0000002408253654"></a>

RNG：支持DRBG，以更高速率获取随机数。

### 摘要算法<a name="ZH-CN_TOPIC_0000002441572917"></a>

HASH：

-   支持SHA256/SHA384/SHA512；
-   支持HMAC256/HMAC384/HMAC512；
-   支持软件多通道，最多可以申请15个软件通道。

### 算法标准<a name="ZH-CN_TOPIC_0000002441653073"></a>

以上各功能模块涉及的算法及工作模式符合以下标准：

-   AES算法的实现符合FIPS 197标准，其支持的工作模式符合以下标准：
    -   ECB、CBC、1/8/128-CFB、128-OFB、CTR几种工作模式符合NIST special800-38a标准
    -   CCM工作模式符合NIST special800-38c标准
    -   GCM工作模式符合NIST special800-38d标准

-   RSA支持公钥加密私钥解密、私钥加密公钥解密、签名及验签等功能，各种模式的数据填充方式符合PKCS\#1标准。支持PKCS\#1 V1.5和PKCS\#1 V2.1填充方式。在加解密模式时，PKCS\#1 V2.1填充方式为OAEP；在签名验签模式时，PKCS\#1 V2.1填充方式为PSS。

>![](public_sys-resources/icon-note.gif) **说明：** 
>-   对称加解密算法的工作模式主要有：
>    ECB（Electronic codebook，电子密码本模式）、CBC（Cipher-block chaining，密码分组链接模式）、CFB（Cipher feedback，密文反馈模式）、OFB（Output feedback，输出反馈模式）、CTR（Counter mode，计数器模式）、CCM（counter with CBC-MAC，CTR加密模式和消息认证码CMAC算法的混合）、GCM（Galois/Counter Mode，伽罗华域/计数器模式），主要由工作在计数器模式下的分组密码和在伽罗华域GF（2^128）上的哈希运算组成。CCM模式在加解密的同时生成CMAC检验值，GCM模式使用GHASH生成认证信息，解密时的CMAC要和加密时的CMAC一样才说明解密是正确的，常用在需要同时加密和认证的领域，欲了解算法的详细内容，请参考相关文献。
>-   块密码学中，将需要加密/解密的消息块分成数块：
>    ECB模式中，对每个块进行独立加密/解密，块与块之间没有依赖；非ECB模式中，块与块之间有依赖性，并且为了保证每条消息的唯一性，在第一个块中需要使用初始化向量IV。

### CIPHER使用注意事项<a name="ZH-CN_TOPIC_0000002408093774"></a>

CIPHER部署在不同场景下时，使用方式可能会有所不同。

-   在LiteOS环境下，链接CIPHER的静态库libss\_cipher.a。
-   在Linux环境下，用户态使用CIPHER可以通过链接静态库libss\_cipher.a或动态库libss\_cipher.so的方式，依赖libsecurec.a或libsecurec.so。内核态CIPHER使用模块插入方式，即insmod ot\_cipher.ko，需要依赖ot\_osal.ko， ot\_base.ko，sys\_config.ko，ot\_sys.ko，此方式CIPHER默认依赖MMZ地址。
-   在OPTEE环境下
    -   用户态调用CIPHER对外接口由Linux环境下的ss\_mpi\_xxx命名形式对应更改为ot\_tee\_xxx；
    -   内核态调用CIPHER对外接口由Linux环境下的ss\_mpi\_xxx命名形式对应更改为ot\_drv\_xxx。

-   在UBOOT环境下，用户态调用CIPHER对外接口由Linux环境下的ss\_mpi\_xxx命名形式对应变更为ot\_mpi\_xxx。

### 规格差异说明<a name="ZH-CN_TOPIC_0000002441572921"></a>

CIPHER支持的AES、HASH、RSA不同解决方案间的配置差异如[表1](#_Ref47627660)所示。

**表 1**  规格差异说明

<a name="_Ref47627660"></a>
<table><thead align="left"><tr id="row153mcpsimp"><th class="cellrowborder" valign="top" width="54%" id="mcps1.2.3.1.1"><p id="p155mcpsimp"><a name="p155mcpsimp"></a><a name="p155mcpsimp"></a>规格差异</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.2.3.1.2"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>SS928V100、SS626V100</p>
</th>
</tr>
</thead>
<tbody><tr id="row159mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p161mcpsimp"><a name="p161mcpsimp"></a><a name="p161mcpsimp"></a>AES (ECB/CBC/CTR/CFB/OFB)</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p163mcpsimp"><a name="p163mcpsimp"></a><a name="p163mcpsimp"></a>支持</p>
</td>
</tr>
<tr id="row164mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p166mcpsimp"><a name="p166mcpsimp"></a><a name="p166mcpsimp"></a>AES (CCM/GCM)</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p168mcpsimp"><a name="p168mcpsimp"></a><a name="p168mcpsimp"></a>支持</p>
</td>
</tr>
<tr id="row169mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p171mcpsimp"><a name="p171mcpsimp"></a><a name="p171mcpsimp"></a>HASH (SHA256)</p>
<p id="p172mcpsimp"><a name="p172mcpsimp"></a><a name="p172mcpsimp"></a>HMAC (SHA256)</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p174mcpsimp"><a name="p174mcpsimp"></a><a name="p174mcpsimp"></a>支持</p>
</td>
</tr>
<tr id="row175mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p177mcpsimp"><a name="p177mcpsimp"></a><a name="p177mcpsimp"></a>HASH (SHA384/SHA512)</p>
<p id="p178mcpsimp"><a name="p178mcpsimp"></a><a name="p178mcpsimp"></a>HMAC (SHA384/SHA512)</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p180mcpsimp"><a name="p180mcpsimp"></a><a name="p180mcpsimp"></a>支持</p>
</td>
</tr>
<tr id="row181mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p183mcpsimp"><a name="p183mcpsimp"></a><a name="p183mcpsimp"></a>RSA 2048/3072/4096</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p185mcpsimp"><a name="p185mcpsimp"></a><a name="p185mcpsimp"></a>支持</p>
</td>
</tr>
<tr id="row186mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p188mcpsimp"><a name="p188mcpsimp"></a><a name="p188mcpsimp"></a>TRNG</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p190mcpsimp"><a name="p190mcpsimp"></a><a name="p190mcpsimp"></a>支持</p>
</td>
</tr>
<tr id="row191mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p193mcpsimp"><a name="p193mcpsimp"></a><a name="p193mcpsimp"></a>SM2</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p195mcpsimp"><a name="p195mcpsimp"></a><a name="p195mcpsimp"></a>不支持</p>
</td>
</tr>
<tr id="row196mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p198mcpsimp"><a name="p198mcpsimp"></a><a name="p198mcpsimp"></a>SM3</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p200mcpsimp"><a name="p200mcpsimp"></a><a name="p200mcpsimp"></a>不支持</p>
</td>
</tr>
<tr id="row201mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.2.3.1.1 "><p id="p203mcpsimp"><a name="p203mcpsimp"></a><a name="p203mcpsimp"></a>SM4</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.2.3.1.2 "><p id="p205mcpsimp"><a name="p205mcpsimp"></a><a name="p205mcpsimp"></a>不支持</p>
</td>
</tr>
</tbody>
</table>

## 使用流程<a name="ZH-CN_TOPIC_0000002408253578"></a>









### 单包数据加解密（对称加解密算法）<a name="ZH-CN_TOPIC_0000002408093702"></a>




#### 场景说明<a name="ZH-CN_TOPIC_0000002441572877"></a>

对单包数据进行加密或解密。当物理内存中有一段码流数据需要进行加/解密时，获取物理地址后在用户层调用CIPHER模块实现加/解密，或当虚拟内存中有一段数据需要进行加/解密时，获取虚拟地址后在用户层调用CIPHER模块实现加/解密。

#### 工作流程<a name="ZH-CN_TOPIC_0000002408093670"></a>

1.  CIPHER设备初始化。调用接口[ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)。
2.  创建CIPHER句柄。调用接口[ss\_mpi\_cipher\_create](#ZH-CN_TOPIC_0000002408253570)。
3.  创建KEYSLOT句柄。调用接口[ss\_mpi\_keyslot\_create](#ZH-CN_TOPIC_0000002441572909)。
4.  绑定CIPHER和KEYSLOT句柄。调用接口[ss\_mpi\_cipher\_attach](#ZH-CN_TOPIC_0000002408093718)。
5.  配置CIPHER控制信息。包含加解密算法、工作模式等信息。调用接口[ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)。
6.  配置密钥。请参考《KLAD API 参考》1.2.1 明文KEY传递或1.2.2 ROOTKEY传递。
7.  加解密数据。用户可调用以下任意接口加解密数据。
    -   物理内存中数据的单包加密--[ss\_mpi\_cipher\_encrypt](#ss_mpi_cipher_encrypt)
    -   物理内存中数据的单包解密--[ss\_mpi\_cipher\_decrypt](#ss_mpi_cipher_decrypt)
    -   虚拟内存中数据的单包加密--[ss\_mpi\_cipher\_encrypt\_virt](#ss_mpi_cipher_encrypt_virt)
    -   虚拟内存中数据的单包解密--[ss\_mpi\_cipher\_decrypt\_virt](#ss_mpi_cipher_decrypt_virt)

8.  解绑定CIPHER和KEYSLOT句柄。调用接口[ss\_mpi\_cipher\_detach](#ZH-CN_TOPIC_0000002441653049)。
9.  销毁KEYSLOT句柄。调用接口[ss\_mpi\_keyslot\_destroy](#ZH-CN_TOPIC_0000002408093686)。
10. 销毁CIPHER句柄。调用接口[ss\_mpi\_cipher\_destroy](#ZH-CN_TOPIC_0000002408253590)。
11. CIPHER设备去初始化。调用接口[ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)。

#### 注意事项<a name="ZH-CN_TOPIC_0000002441653001"></a>

使用CIPHER模块时，请特别注意以下几点。

-   该接口支持AES对称加解密算法。
-   各算法支持ECB/CBC/CFB/OFB/CTR/CCM/GCM等工作模式。CCM/GCM工作模式加解密请参考“[CCM/GCM加解密（对称加解密算法）](#ZH-CN_TOPIC_0000002441653033)”章节。
-   在进行加密、解密运算前必须先获取CIPHER句柄，当长时间不使用时可以释放，建议加密、解密各获取一个句柄，每个句柄只进行加密或者只进行解密操作。
-   支持对不带cache的物理空间连续的内存数据进行加密、解密（如果是带cache的，需要用户自己执行刷cache操作）和对虚拟空间的内存数据进行加密、解密（用户可以使用malloc等申请虚拟地址）。
-   CIPHER内部采用DMA方式传输数据，所以调用[ss\_mpi\_cipher\_encrypt](#ZH-CN_TOPIC_0000002441652993)或[ss\_mpi\_cipher\_decrypt](#ZH-CN_TOPIC_0000002441572865)接口进行数据的加密或解密时，传入的地址参数为数据的物理地址。当调用[ss\_mpi\_cipher\_encrypt\_virt](#ZH-CN_TOPIC_0000002408253614)或[ss\_mpi\_cipher\_decrypt\_virt](#ZH-CN_TOPIC_0000002441572833)接口进行数据的加密或解密时，传入的地址参数为数据的虚拟地址。
-   加密、解密的源地址、目的地址可以相同，即可以在原地（密文、明文使用同一块buffer）进行数据的加密和解密。
-   使用非ECB模式进行CIPHER的加解密时，需要使用初始化向量IV（Initial Vector）。
-   配置IV时有以下两个场景（以解密数据块为例）：

    **【场景1】**

    每次调用CIPHER时都需要更新IV，此时请设置chg\_flags = OT\_CIPHER\_IV\_CHG\_ALL\_PACK，并正确配置IV值。

    函数调用顺序请参考：

    ```
    ss_mpi_cipher_set_cfg()  // should set chg_flags = OT_CIPHER_IV_CHG_ALL_PACK and update iv
    ss_mpi_cipher_decrypt()
    ss_mpi_cipher_set_cfg()  // should set chg_flags = OT_CIPHER_IV_CHG_ALL_PACK and update iv
    ss_mpi_cipher_decrypt()
    ….
    ss_mpi_cipher_set_cfg()  // should set chg_flags = OT_CIPHER_IV_CHG_ALL_PACK and update iv
    ss_mpi_cipher_decrypt()
    ```

    **图 1**  CIPHER应用场景1，每次调用都需要更新IV<a name="fig134088540378"></a>  
    ![](figures/CIPHER应用场景1-每次调用都需要更新IV.png "CIPHER应用场景1-每次调用都需要更新IV")

    **【场景2】**

    只需第一次调用CIPHER时设置IV，此时请设置chg\_flags = OT\_CIPHER\_IV\_CHG\_ONE\_PACK，且配置IV值。

    函数调用顺序请参考：

    ```
    ss_mpi_cipher_set_cfg()  // should set chg_flags = OT_CIPHER_IV_CHG_ONE_PACK and update iv
    ss_mpi_cipher_decrypt()
    ss_mpi_cipher_decrypt()
    ss_mpi_cipher_decrypt()
    ```

    **图 2**  CIPHER应用场景2，只在第一次调用时配置IV<a name="fig45629317391"></a>  
    ![](figures/CIPHER应用场景2-只在第一次调用时配置IV.png "CIPHER应用场景2-只在第一次调用时配置IV")

    请结合实际场景进行IV的配置。

-   单包加解密的IV向量可继承。创建一路CIPHER，配置属性（假设配置的工作模式需要使用IV向量）之后，每次调用单包加解密接口时，IV向量会依次轮流使用。

    例如：用户需依次加密数据0，数据1。向量为a,b,c,d。用户加密完数据0之后，数据0的最后一个分块数据使用了IV向量中的b进行加密处理；此时，用户再加密数据1时，数据1的第一个分块数据将会使用IV向量c进行加密，然后依次为d,a,b,c,d…。

    因此在加解密时，必须要保证两次向量使用的一致性。重新配置CIPHER控制信息将设置IV向量从第一个开始

-   CCM、GCM在计算完成后需要获取TAG值，解密的TAG要和加密时一样解密才成功。

### 多包数据加解密（对称加解密算法）<a name="ZH-CN_TOPIC_0000002408253610"></a>




#### 场景说明<a name="ZH-CN_TOPIC_0000002441572933"></a>

对多个数据包进行加密或解密。当物理内存中有多段码流数据需要进行加/解密时，获取物理地址后在用户层调用CIPHER模块实现加/解密。

#### 工作流程<a name="ZH-CN_TOPIC_0000002441652989"></a>

1.  CIPHER设备初始化。调用接口[ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)。
2.  创建CIPHER句柄。调用接口[ss\_mpi\_cipher\_create](#ZH-CN_TOPIC_0000002408253570)。
3.  创建KEYSLOT句柄。调用接口[ss\_mpi\_keyslot\_create](#ZH-CN_TOPIC_0000002441572909)。
4.  绑定CIPHER和KEYSLOT句柄。调用接口[ss\_mpi\_cipher\_attach](#ZH-CN_TOPIC_0000002408093718)。
5.  配置CIPHER控制信息。包含加解密算法、工作模式等信息。调用接口[ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)。
6.  配置密钥。请参考《KLAD API 参考》1.2.1 明文KEY传递或1.2.2 ROOTKEY传递。
7.  加解密数据。用户可调用以下任意接口加解密数据。
    -   多包加密--[ss\_mpi\_cipher\_encrypt\_multi\_pack](#ss_mpi_cipher_encrypt_multi_pack)
    -   多包解密--[ss\_mpi\_cipher\_decrypt\_multi\_pack](#ss_mpi_cipher_decrypt_multi_pack)

8.  解绑定CIPHER和KEYSLOT句柄。调用接口[ss\_mpi\_cipher\_detach](#ZH-CN_TOPIC_0000002441653049)。
9.  销毁KEYSLOT句柄。调用接口[ss\_mpi\_keyslot\_destroy](#ZH-CN_TOPIC_0000002408093686)。
10. 销毁CIPHER句柄。调用接口[ss\_mpi\_cipher\_destroy](#ZH-CN_TOPIC_0000002408253590)。
11. CIPHER设备去初始化。调用接口[ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)。

#### 注意事项<a name="ZH-CN_TOPIC_0000002441572861"></a>

-   进行多包加解密时，最多支持同时加解密5000个包。
-   对于多个包的操作，每个包都使用[ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)配置的向量进行运算，IV作用域是可配置的，前一个包的向量运算结果可以作为下一个包的IV，或者每个包IV都是独立运算的（前一次函数调用的结果不会影响后一次函数调用的运算结果）。
-   进行多包加解密时，需要使用物理地址作为地址参数。
-   其它注意事项同“[单包数据加解密（对称加解密算法）](#ZH-CN_TOPIC_0000002408093702)”章节。

### CCM/GCM加解密（对称加解密算法）<a name="ZH-CN_TOPIC_0000002441653033"></a>




#### 场景说明<a name="ZH-CN_TOPIC_0000002441572893"></a>

对数据进行CCM加解密。该算法请参考：SP800-38C\_updated-July20\_2007\_CCM. The CCM Mode for Authentication and Confidentiality。

对数据进行GCM加解密。该算法请参考：SP-800-38D-GCM. Galois/Counter Mode \(GCM\) and GMAC。

#### 工作流程<a name="ZH-CN_TOPIC_0000002441572849"></a>

1.  CIPHER设备初始化。调用接口[ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)。
2.  创建CIPHER句柄。调用接口[ss\_mpi\_cipher\_create](#ZH-CN_TOPIC_0000002408253570)。
3.  创建KEYSLOT句柄。调用接口[ss\_mpi\_keyslot\_create](#ZH-CN_TOPIC_0000002441572909)。
4.  绑定CIPHER和KEYSLOT句柄。调用接口[ss\_mpi\_cipher\_attach](#ZH-CN_TOPIC_0000002408093718)。
5.  配置CIPHER控制信息。包含加解密算法、工作模式等信息。调用接口[ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)。
6.  配置密钥。请参考《KLAD API 参考》1.2.1 明文KEY传递或1.2.2 ROOTKEY传递。
7.  加解密数据。用户可调用以下任意接口加解密数据。
    -   物理内存中数据加密--[ss\_mpi\_cipher\_encrypt](#ss_mpi_cipher_encrypt)
    -   物理内存中数据解密--[ss\_mpi\_cipher\_decrypt](#ss_mpi_cipher_decrypt)
    -   虚拟内存中数据加密--[ss\_mpi\_cipher\_encrypt\_virt](#ss_mpi_cipher_encrypt_virt)
    -   虚拟内存中数据解密--[ss\_mpi\_cipher\_decrypt\_virt](#ss_mpi_cipher_decrypt_virt)

8.  获取TAG值。调用接口[ss\_mpi\_cipher\_get\_tag](#ZH-CN_TOPIC_0000002441653053)。
9.  解绑定CIPHER和KEYSLOT句柄。调用接口[ss\_mpi\_cipher\_detach](#ZH-CN_TOPIC_0000002441653049)。
10. 销毁KEYSLOT句柄。调用接口[ss\_mpi\_keyslot\_destroy](#ZH-CN_TOPIC_0000002408093686)。
11. 销毁CIPHER句柄。调用接口[ss\_mpi\_cipher\_destroy](#ZH-CN_TOPIC_0000002408253590)。
12. CIPHER设备去初始化。调用接口[ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)。

#### 注意事项<a name="ZH-CN_TOPIC_0000002441653021"></a>

-   CCM/GCM密钥长度为128/192/256 bits\(硬件 key 只支持 128/256 bits\)。CCM/GCM解密产生的TAG值必须和加密时一样，解密结果才是正确的。
-   AES-CCM模式由AES CTR加密模式和CBC-MAC认证算法构成，既可以保证数据的保密性，也能保证数据的完整性。
    -   根据CCM算法原理，向量IV长度iv\_len可取\{7, 8, 9, 10, 11, 12, 13\} bytes，IV存放算法标准中的Nonce数据N，加密数据的长度用n个Byte表示，且应满足条件：iv\_len+n=15, 所以iv\_len为13时，n为2，此时加密数据长度最长为65535bytes，其它以此类推。
    -   CCM加密时的向量N、关联数据A取值必须与解密时保持一致。

-   AES-GCM模式由AES CTR和GHASH构成，既可以保证数据的保密性，也能保证数据的完整性。
    -   根据GCM算法原理，GCM的向量IV长度iv\_len可取范围为\[1\~16\]。
    -   GCM加密时的关联数据A取值必须与解密时保持一致。

### HASH计算（摘要算法）<a name="ZH-CN_TOPIC_0000002408253626"></a>




#### 场景说明<a name="ZH-CN_TOPIC_0000002441572829"></a>

计算数据的HASH值，可选择SHA256/SHA384/SHA512。

#### 工作流程<a name="ZH-CN_TOPIC_0000002408253594"></a>

1.  CIPHER设备初始化。调用接口[ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)完成。
2.  <a name="li16799101725513"></a>创建一路HASH，获取HASH句柄，选择HASH算法。调用接口[ss\_mpi\_cipher\_hash\_init](#ZH-CN_TOPIC_0000002408093678)完成。
3.  <a name="li579917172559"></a>输入数据，逐个数据块依次计算HASH值。调用接口[ss\_mpi\_cipher\_hash\_update](#ZH-CN_TOPIC_0000002408253598)完成。
4.  如果摘要未计算完成，再次执行[3](#li579917172559)。
5.  <a name="li379991710553"></a>完成摘要计算，结束输入，获取计算结果。调用接口[ss\_mpi\_cipher\_hash\_final](#ZH-CN_TOPIC_0000002408093722)完成。
6.  关闭CIPHER设备。调用接口[ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)完成。

#### 注意事项<a name="ZH-CN_TOPIC_0000002441572881"></a>

支持软件多通道，可同时进行多个HASH运算， 即执行[2](#li16799101725513)启动一个HASH运算，在本次HASH计算未完成（即未执行[5](#li379991710553)）之前，可申请一个新通道启动另一个HASH运算，直到申请不到通道为止。

最多支持15个HASH软件通道，15个通道可同时都被打开，但同一时间内只有一个通道在进行运算。

### HMAC计算（摘要算法）<a name="ZH-CN_TOPIC_0000002408093738"></a>




#### 场景说明<a name="ZH-CN_TOPIC_0000002408253646"></a>

计算数据的HMAC值。基于的HASH算法为 SHA256/SHA384/SHA512。

#### 工作流程<a name="ZH-CN_TOPIC_0000002441572869"></a>

HMAC运算开发操作步骤如下：

1.  调用[ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)初始化CIPHER模块。
2.  <a name="li132961530185714"></a>调用[ss\_mpi\_cipher\_hash\_init](#ZH-CN_TOPIC_0000002408093678)选择使用的HASH算法，并配置HMAC计算的密钥，初始化HASH模块。
3.  调用[ss\_mpi\_cipher\_hash\_update](#ZH-CN_TOPIC_0000002408253598)输入数据，可以一个BLOCK接一个BLOCK输入。
4.  <a name="li19296113055717"></a>调用[ss\_mpi\_cipher\_hash\_final](#ZH-CN_TOPIC_0000002408093722)结束输入，并输出HMAC值。
5.  调用[ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)  去初始化CIPHER设备。

#### 注意事项<a name="ZH-CN_TOPIC_0000002441653081"></a>

支持软件多通道，可同时进行多个HMAC运算， 即执行[2](#li132961530185714)启动一个HMAC运算，在本次HMAC计算未完成（即未执行[4](#li19296113055717)）之前，可申请一个新通道启动另一个HMAC运算，直到申请不到通道为止。

HMAC和HASH共用15个软件通道，15个通道可同时都被打开，但同一时间内只有一个通道在进行运算。

### 随机数生成<a name="ZH-CN_TOPIC_0000002408093746"></a>




#### 场景说明<a name="ZH-CN_TOPIC_0000002441652997"></a>

获取硬件产生的真随机数。

#### 工作流程<a name="ZH-CN_TOPIC_0000002441653029"></a>

生成随机数据的过程如下：

1.  CIPHER设备初始化。调用接口[ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)完成。
2.  获取32bits的随机数。调用接口[ss\_mpi\_cipher\_get\_random\_num](#ZH-CN_TOPIC_0000002408253630)完成。
3.  关闭CIPHER设备。调用接口[ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)完成。

#### 注意事项<a name="ZH-CN_TOPIC_0000002408253634"></a>

无。

### RSA加解密（不对称加解密算法）<a name="ZH-CN_TOPIC_0000002441652977"></a>




#### 场景说明<a name="ZH-CN_TOPIC_0000002408253574"></a>

对数据进行RSA不对称算法进行加解密，当使用公钥加密的数据，必须使用私钥进行解密，反之，使用私钥加密的数据，必须使用公钥进行解密。

该算法请参考：rfc3447. RSA Cryptography Specifications。

#### 工作流程<a name="ZH-CN_TOPIC_0000002408093726"></a>

对数据进行不对称的RSA加解密的过程如下：

1.  CIPHER设备初始化。调用接口[ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)完成。
2.  对数据进行加解密。根据使用的密钥不同，分为4个接口，用户可以调用以下任一接口进行加解密等。
    -   公钥加密--  [ss\_mpi\_cipher\_rsa\_public\_encrypt](#ss_mpi_cipher_rsa_public_encrypt)
    -   私钥解密--  [ss\_mpi\_cipher\_rsa\_private\_decrypt](#ss_mpi_cipher_rsa_private_decrypt)
    -   私钥加密--  [ss\_mpi\_cipher\_rsa\_private\_encrypt](#ss_mpi_cipher_rsa_private_encrypt)
    -   公钥解密--  [ss\_mpi\_cipher\_rsa\_public\_decrypt](#ss_mpi_cipher_rsa_public_decrypt)

3.  关闭CIPHER设备。调用接口[ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)完成。

#### 注意事项<a name="ZH-CN_TOPIC_0000002408253670"></a>

RSA密钥位宽可选2048、3072及4096。根据RSA算法原理，明文和密文都必须比公钥N小，所以待加解密的数据长度必须小于或等于密钥的长度，惯用 做法是在待加解密的数据的高位补0等，使其长度和公钥N相等，但其值比公钥N小。支持PKCS\#1 V1.5和PKCS\#1 V2.1填充方式，其中PKCS\#1 V1.5为弱填充方式，客户不建议使用该填充方式，PKCS\#1 V2.1填充方式为OAEP。注意：op-tee、uboot环境不支持RSA私钥，priv\_key用p/q/dp/dq/qp代替d。

### RSA签名及验签（不对称加解密算法）<a name="ZH-CN_TOPIC_0000002408093674"></a>




#### 场景说明<a name="ZH-CN_TOPIC_0000002441653017"></a>

对数据进行RSA签名及验签时，使用私钥进行数据签名，使用公钥进行数据验签。

该算法请参考：rfc3447. RSA Cryptography Specifications。

#### 工作流程<a name="ZH-CN_TOPIC_0000002408093734"></a>

对数据进行不对称的RSA签名及验签的过程如下：

1.  CIPHER设备初始化。调用接口[ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)完成。
2.  对数据进行签名验证，调用以下接口签名验证。
    -   私钥签名--[ss\_mpi\_cipher\_rsa\_sign](#ss_mpi_cipher_rsa_sign)
    -   公钥验证--[ss\_mpi\_cipher\_rsa\_verify](#ss_mpi_cipher_rsa_verify)

3.  关闭CIPHER设备。调用接口[ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)完成。

#### 注意事项<a name="ZH-CN_TOPIC_0000002441653065"></a>

RSA密钥位宽可选2048、3072及4096。根据RSA算法原理，明文和密文都必须比公钥小，所以待加解密的数据长度必须小于或等于密钥的长度，惯用作法是先计算待签名数据的HASH值，接着将HASH值填充成长度和公钥N相等但其值比公钥N小的数据，然后再进行加密。支持PKCS\#1 V1.5和PKCS\#1 V2.1填充方式，其中PKCS\#1 V1.5为弱填充方式，客户不要该填充方式，PKCS\#1 V2.1填充方式为PSS。注意：op-tee、uboot环境不支持RSA私钥，priv\_key用p/q/dp/dq/qp代替d。

# API参考
CIPHER提供以下API：

-   [ss\_mpi\_cipher\_init](#ZH-CN_TOPIC_0000002408093694)：初始化CIPHER模块。
-   [ss\_mpi\_cipher\_deinit](#ZH-CN_TOPIC_0000002441572905)：去初始化CIPHER模块。
-   [ss\_mpi\_cipher\_create](#ZH-CN_TOPIC_0000002408253570)：对称加解密时创建一路的CIPHER句柄。
-   [ss\_mpi\_cipher\_destroy](#ZH-CN_TOPIC_0000002408253590)：对称加解密时销毁已存在的CIPHER句柄。
-   [ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)：对称加解密时配置CIPHER通道对应的控制信息。
-   [ss\_mpi\_cipher\_get\_cfg](#ZH-CN_TOPIC_0000002441572913)：对称加解密时获取CIPHER通道对应的配置信息。
-   [ss\_mpi\_cipher\_encrypt](#ZH-CN_TOPIC_0000002441652993)：对称加解密时单包数据加密功能。
-   [ss\_mpi\_cipher\_decrypt](#ZH-CN_TOPIC_0000002441572865)：对称加解密时单包数据解密功能。
-   [ss\_mpi\_cipher\_encrypt\_virt](#ZH-CN_TOPIC_0000002408253614)：对称加解密时对数据进行加密。
-   [ss\_mpi\_cipher\_decrypt\_virt](#ZH-CN_TOPIC_0000002441572833)：对称加解密时对数据进行解密。
-   [ss\_mpi\_cipher\_encrypt\_multi\_pack](#ZH-CN_TOPIC_0000002408093690)：对称加解密时多包数据加密功能。
-   [ss\_mpi\_cipher\_decrypt\_multi\_pack](#ZH-CN_TOPIC_0000002441653025)：对称加解密时多包数据解密功能。
-   [ss\_mpi\_cipher\_get\_tag](#ZH-CN_TOPIC_0000002441653053)：对称加解密时CCM/GCM模式获取TAG值。
-   [ss\_mpi\_cipher\_hash\_init](#ZH-CN_TOPIC_0000002408093678)：HASH、HMAC计算初始化功能。
-   [ss\_mpi\_cipher\_hash\_update](#ZH-CN_TOPIC_0000002408253598)：HASH、HMAC计算数据输入功能。
-   [ss\_mpi\_cipher\_hash\_final](#ZH-CN_TOPIC_0000002408093722)：HASH、HMAC计算最终结果输出功能。
-   [ss\_mpi\_cipher\_get\_random\_num](#ZH-CN_TOPIC_0000002408253630)：获取随机数功能。
-   [ss\_mpi\_cipher\_rsa\_public\_encrypt](#ZH-CN_TOPIC_0000002408253586)：使用RSA公钥加密一段明文。
-   [ss\_mpi\_cipher\_rsa\_private\_decrypt](#ZH-CN_TOPIC_0000002408093710)：使用RSA私钥解密一段密文。
-   [ss\_mpi\_cipher\_rsa\_private\_encrypt](#ZH-CN_TOPIC_0000002441653041)：使用RSA私钥加密一段明文。
-   [ss\_mpi\_cipher\_rsa\_public\_decrypt](#ZH-CN_TOPIC_0000002408253566)：使用RSA公钥解密一段密文。
-   [ss\_mpi\_cipher\_rsa\_sign](#ZH-CN_TOPIC_0000002441653009)：使用RSA私钥签名一段文本。
-   [ss\_mpi\_cipher\_rsa\_verify](#ZH-CN_TOPIC_0000002408253618)：使用RSA公钥验证一段文本。
-   [ss\_mpi\_cipher\_sm2\_encrypt](#ZH-CN_TOPIC_0000002441572901)：使用SM2公钥加密一段明文。
-   [ss\_mpi\_cipher\_sm2\_decrypt](#ZH-CN_TOPIC_0000002441653061)：使用SM2私钥解密一段密文。
-   [ss\_mpi\_cipher\_sm2\_sign](#ZH-CN_TOPIC_0000002408253606)：使用SM2签名一段文本。
-   [ss\_mpi\_cipher\_sm2\_verify](#ZH-CN_TOPIC_0000002408093770)：使用SM2验证一段文本。
-   [ss\_mpi\_keyslot\_create](#ZH-CN_TOPIC_0000002441572909)：对称加解密时创建一路keyslot句柄。
-   [ss\_mpi\_keyslot\_destroy](#ZH-CN_TOPIC_0000002408093686)：对称加解密时销毁一路keyslot句柄。
-   [ss\_mpi\_cipher\_attach](#ZH-CN_TOPIC_0000002408093718)：对称加解密时cipher句柄与keyslot句柄绑定。
-   [ss\_mpi\_cipher\_detach](#ZH-CN_TOPIC_0000002441653049)：对称加解密时cipher句柄与keyslot句柄解绑定。
































## ss\_mpi\_cipher\_init<a name="ZH-CN_TOPIC_0000002408093694"></a>

【描述】

初始化CIPHER模块。

【语法】

```
td_s32 ss_mpi_cipher_init(td_void);
```

【参数】

无。

【返回值】

<a name="table535mcpsimp"></a>
<table><thead align="left"><tr id="row540mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p542mcpsimp"><a name="p542mcpsimp"></a><a name="p542mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p544mcpsimp"><a name="p544mcpsimp"></a><a name="p544mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row546mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p548mcpsimp"><a name="p548mcpsimp"></a><a name="p548mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p550mcpsimp"><a name="p550mcpsimp"></a><a name="p550mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row551mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p553mcpsimp"><a name="p553mcpsimp"></a><a name="p553mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p555mcpsimp"><a name="p555mcpsimp"></a><a name="p555mcpsimp"></a>参见<a href="#ZH-CN_TOPIC_0000002408253662">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   支持多次调用。
-   初始化和去初始化成对使用。
-   内核态不需要调用此接口。

【举例】

无。

## ss\_mpi\_cipher\_deinit<a name="ZH-CN_TOPIC_0000002441572905"></a>

【描述】

去初始化CIPHER模块。

【语法】

```
td_s32 ss_mpi_cipher_deinit(td_void);
```

【参数】

无。

【返回值】

<a name="table575mcpsimp"></a>
<table><thead align="left"><tr id="row580mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p582mcpsimp"><a name="p582mcpsimp"></a><a name="p582mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p584mcpsimp"><a name="p584mcpsimp"></a><a name="p584mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row586mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p588mcpsimp"><a name="p588mcpsimp"></a><a name="p588mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p590mcpsimp"><a name="p590mcpsimp"></a><a name="p590mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row591mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p593mcpsimp"><a name="p593mcpsimp"></a><a name="p593mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p595mcpsimp"><a name="p595mcpsimp"></a><a name="p595mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   支持多次调用。
-   初始化和去初始化成对使用。

【举例】

无。

## ss\_mpi\_cipher\_create<a name="ZH-CN_TOPIC_0000002408253570"></a>

【描述】

对称算法加解密时创建的CIPHER句柄。

【语法】

```
td_s32 ss_mpi_cipher_create (td_handle *handle, const ot_cipher_attr *cipher_attr);
```

【参数】

<a name="table615mcpsimp"></a>
<table><thead align="left"><tr id="row621mcpsimp"><th class="cellrowborder" valign="top" width="17.82%" id="mcps1.1.4.1.1"><p id="p623mcpsimp"><a name="p623mcpsimp"></a><a name="p623mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="65.35%" id="mcps1.1.4.1.2"><p id="p625mcpsimp"><a name="p625mcpsimp"></a><a name="p625mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.1.4.1.3"><p id="p627mcpsimp"><a name="p627mcpsimp"></a><a name="p627mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row629mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p id="p631mcpsimp"><a name="p631mcpsimp"></a><a name="p631mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65.35%" headers="mcps1.1.4.1.2 "><p id="p633mcpsimp"><a name="p633mcpsimp"></a><a name="p633mcpsimp"></a>CIPHER句柄指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.1.4.1.3 "><p id="p635mcpsimp"><a name="p635mcpsimp"></a><a name="p635mcpsimp"></a>输出</p>
</td>
</tr>
<tr id="row636mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p id="p638mcpsimp"><a name="p638mcpsimp"></a><a name="p638mcpsimp"></a>cipher_attr</p>
</td>
<td class="cellrowborder" valign="top" width="65.35%" headers="mcps1.1.4.1.2 "><p id="p640mcpsimp"><a name="p640mcpsimp"></a><a name="p640mcpsimp"></a>CIPHER属性指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.1.4.1.3 "><p id="p642mcpsimp"><a name="p642mcpsimp"></a><a name="p642mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table644mcpsimp"></a>
<table><thead align="left"><tr id="row649mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p651mcpsimp"><a name="p651mcpsimp"></a><a name="p651mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p653mcpsimp"><a name="p653mcpsimp"></a><a name="p653mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row655mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p657mcpsimp"><a name="p657mcpsimp"></a><a name="p657mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p659mcpsimp"><a name="p659mcpsimp"></a><a name="p659mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row660mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p662mcpsimp"><a name="p662mcpsimp"></a><a name="p662mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p664mcpsimp"><a name="p664mcpsimp"></a><a name="p664mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   handle、cipher\_attr不能为空。
-   SS928V100、SS626V100支持15路CIPHER通道。
-   使用完通道后，应销毁对应的通道。

【举例】

无。

## ss\_mpi\_cipher\_destroy<a name="ZH-CN_TOPIC_0000002408253590"></a>

【描述】

对称算法加解密时销毁的CIPHER句柄。

【语法】

```
td_s32 ss_mpi_cipher_destroy (td_handle handle);
```

【参数】

<a name="table683mcpsimp"></a>
<table><thead align="left"><tr id="row689mcpsimp"><th class="cellrowborder" valign="top" width="17.82%" id="mcps1.1.4.1.1"><p id="p691mcpsimp"><a name="p691mcpsimp"></a><a name="p691mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="65.35%" id="mcps1.1.4.1.2"><p id="p693mcpsimp"><a name="p693mcpsimp"></a><a name="p693mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.1.4.1.3"><p id="p695mcpsimp"><a name="p695mcpsimp"></a><a name="p695mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row697mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p id="p699mcpsimp"><a name="p699mcpsimp"></a><a name="p699mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65.35%" headers="mcps1.1.4.1.2 "><p id="p701mcpsimp"><a name="p701mcpsimp"></a><a name="p701mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.1.4.1.3 "><p id="p703mcpsimp"><a name="p703mcpsimp"></a><a name="p703mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table705mcpsimp"></a>
<table><thead align="left"><tr id="row710mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p712mcpsimp"><a name="p712mcpsimp"></a><a name="p712mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p714mcpsimp"><a name="p714mcpsimp"></a><a name="p714mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row716mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p718mcpsimp"><a name="p718mcpsimp"></a><a name="p718mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p720mcpsimp"><a name="p720mcpsimp"></a><a name="p720mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row721mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p723mcpsimp"><a name="p723mcpsimp"></a><a name="p723mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p725mcpsimp"><a name="p725mcpsimp"></a><a name="p725mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

创建与销毁通道成对使用。

【举例】

无。

## ss\_mpi\_cipher\_set\_cfg<a name="ZH-CN_TOPIC_0000002408253622"></a>

【描述】

对称加解密时配置CIPHER通道对应的信息。详细配置请参见结构体[ot\_cipher\_ctrl](#ZH-CN_TOPIC_0000002441652985)。

【语法】

```
td_s32 ss_mpi_cipher_set_cfg (td_handle handle, const ot_cipher_ctrl *ctrl);
```

【参数】

<a name="table745mcpsimp"></a>
<table><thead align="left"><tr id="row751mcpsimp"><th class="cellrowborder" valign="top" width="17.82%" id="mcps1.1.4.1.1"><p id="p753mcpsimp"><a name="p753mcpsimp"></a><a name="p753mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="65.35%" id="mcps1.1.4.1.2"><p id="p755mcpsimp"><a name="p755mcpsimp"></a><a name="p755mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.1.4.1.3"><p id="p757mcpsimp"><a name="p757mcpsimp"></a><a name="p757mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row759mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p id="p761mcpsimp"><a name="p761mcpsimp"></a><a name="p761mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65.35%" headers="mcps1.1.4.1.2 "><p id="p763mcpsimp"><a name="p763mcpsimp"></a><a name="p763mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.1.4.1.3 "><p id="p765mcpsimp"><a name="p765mcpsimp"></a><a name="p765mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row766mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p id="p768mcpsimp"><a name="p768mcpsimp"></a><a name="p768mcpsimp"></a>ctrl</p>
</td>
<td class="cellrowborder" valign="top" width="65.35%" headers="mcps1.1.4.1.2 "><p id="p770mcpsimp"><a name="p770mcpsimp"></a><a name="p770mcpsimp"></a>控制信息指针。</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.1.4.1.3 "><p id="p772mcpsimp"><a name="p772mcpsimp"></a><a name="p772mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table774mcpsimp"></a>
<table><thead align="left"><tr id="row779mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p781mcpsimp"><a name="p781mcpsimp"></a><a name="p781mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p783mcpsimp"><a name="p783mcpsimp"></a><a name="p783mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row785mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p787mcpsimp"><a name="p787mcpsimp"></a><a name="p787mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p789mcpsimp"><a name="p789mcpsimp"></a><a name="p789mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row790mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p792mcpsimp"><a name="p792mcpsimp"></a><a name="p792mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p794mcpsimp"><a name="p794mcpsimp"></a><a name="p794mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   ctrl不能为空。

【举例】

无。

## ss\_mpi\_cipher\_get\_cfg<a name="ZH-CN_TOPIC_0000002441572913"></a>

【描述】

对称加解密时获取CIPHER通道对应的配置信息。

【语法】

```
td_s32 ss_mpi_cipher_get_cfg(td_handle handle, ot_cipher_ctrl *ctrl);
```

【参数】

<a name="table814mcpsimp"></a>
<table><thead align="left"><tr id="row820mcpsimp"><th class="cellrowborder" valign="top" width="17.82%" id="mcps1.1.4.1.1"><p id="p822mcpsimp"><a name="p822mcpsimp"></a><a name="p822mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="65.35%" id="mcps1.1.4.1.2"><p id="p824mcpsimp"><a name="p824mcpsimp"></a><a name="p824mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16.830000000000002%" id="mcps1.1.4.1.3"><p id="p826mcpsimp"><a name="p826mcpsimp"></a><a name="p826mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row828mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p id="p830mcpsimp"><a name="p830mcpsimp"></a><a name="p830mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65.35%" headers="mcps1.1.4.1.2 "><p id="p832mcpsimp"><a name="p832mcpsimp"></a><a name="p832mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.1.4.1.3 "><p id="p834mcpsimp"><a name="p834mcpsimp"></a><a name="p834mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row835mcpsimp"><td class="cellrowborder" valign="top" width="17.82%" headers="mcps1.1.4.1.1 "><p id="p837mcpsimp"><a name="p837mcpsimp"></a><a name="p837mcpsimp"></a>ctrl</p>
</td>
<td class="cellrowborder" valign="top" width="65.35%" headers="mcps1.1.4.1.2 "><p id="p839mcpsimp"><a name="p839mcpsimp"></a><a name="p839mcpsimp"></a>CIPHER通道的配置信息。</p>
</td>
<td class="cellrowborder" valign="top" width="16.830000000000002%" headers="mcps1.1.4.1.3 "><p id="p841mcpsimp"><a name="p841mcpsimp"></a><a name="p841mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table843mcpsimp"></a>
<table><thead align="left"><tr id="row848mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p850mcpsimp"><a name="p850mcpsimp"></a><a name="p850mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p852mcpsimp"><a name="p852mcpsimp"></a><a name="p852mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row854mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p856mcpsimp"><a name="p856mcpsimp"></a><a name="p856mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p858mcpsimp"><a name="p858mcpsimp"></a><a name="p858mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row859mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p861mcpsimp"><a name="p861mcpsimp"></a><a name="p861mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p863mcpsimp"><a name="p863mcpsimp"></a><a name="p863mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   ctrl不能为空。

【举例】

无。

## ss\_mpi\_cipher\_encrypt<a name="ZH-CN_TOPIC_0000002441652993"></a>

【描述】

对称加解密时对物理内存数据进行加密。

【语法】

```
td_s32 ss_mpi_cipher_encrypt(td_handle handle, td_phys_addr_t src_phys_addr, td_phys_addr_t dst_phys_addr, td_u32 byte_len);
```

【参数】

<a name="table882mcpsimp"></a>
<table><thead align="left"><tr id="row888mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p890mcpsimp"><a name="p890mcpsimp"></a><a name="p890mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p892mcpsimp"><a name="p892mcpsimp"></a><a name="p892mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p894mcpsimp"><a name="p894mcpsimp"></a><a name="p894mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row896mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p898mcpsimp"><a name="p898mcpsimp"></a><a name="p898mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p900mcpsimp"><a name="p900mcpsimp"></a><a name="p900mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p902mcpsimp"><a name="p902mcpsimp"></a><a name="p902mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row903mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p905mcpsimp"><a name="p905mcpsimp"></a><a name="p905mcpsimp"></a>src_phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p907mcpsimp"><a name="p907mcpsimp"></a><a name="p907mcpsimp"></a>源数据（待加密的数据）的物理地址。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p909mcpsimp"><a name="p909mcpsimp"></a><a name="p909mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row910mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p912mcpsimp"><a name="p912mcpsimp"></a><a name="p912mcpsimp"></a>dst_phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p914mcpsimp"><a name="p914mcpsimp"></a><a name="p914mcpsimp"></a>存放加密结果的物理地址。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p916mcpsimp"><a name="p916mcpsimp"></a><a name="p916mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row917mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p919mcpsimp"><a name="p919mcpsimp"></a><a name="p919mcpsimp"></a>byte_len</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p921mcpsimp"><a name="p921mcpsimp"></a><a name="p921mcpsimp"></a>数据的长度（单位：byte）。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p923mcpsimp"><a name="p923mcpsimp"></a><a name="p923mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table925mcpsimp"></a>
<table><thead align="left"><tr id="row930mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p932mcpsimp"><a name="p932mcpsimp"></a><a name="p932mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p934mcpsimp"><a name="p934mcpsimp"></a><a name="p934mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row936mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p938mcpsimp"><a name="p938mcpsimp"></a><a name="p938mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p940mcpsimp"><a name="p940mcpsimp"></a><a name="p940mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row941mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p943mcpsimp"><a name="p943mcpsimp"></a><a name="p943mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p945mcpsimp"><a name="p945mcpsimp"></a><a name="p945mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   可多次调用，需配合  [ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)  使用，使用方法可参考  [注意事项](#ZH-CN_TOPIC_0000002441653065)。
-   模式为CTR/CCM/GCM时数据的长度为任意长度，其他模式要求block对齐。
-   加密源地址、目的地址可以相同。
-   optee平台不支持。

【举例】

无。

## ss\_mpi\_cipher\_decrypt<a name="ZH-CN_TOPIC_0000002441572865"></a>

【描述】

对称加解密时对物理内存数据进行解密。

【语法】

```
td_s32 ss_mpi_cipher_decrypt(td_handle handle, td_phys_addr_t src_phys_addr, td_phys_addr_t dst_phys_addr, td_u32 byte_len);
```

【参数】

<a name="table966mcpsimp"></a>
<table><thead align="left"><tr id="row972mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p974mcpsimp"><a name="p974mcpsimp"></a><a name="p974mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.2"><p id="p976mcpsimp"><a name="p976mcpsimp"></a><a name="p976mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p978mcpsimp"><a name="p978mcpsimp"></a><a name="p978mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row980mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p982mcpsimp"><a name="p982mcpsimp"></a><a name="p982mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p984mcpsimp"><a name="p984mcpsimp"></a><a name="p984mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p986mcpsimp"><a name="p986mcpsimp"></a><a name="p986mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row987mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p989mcpsimp"><a name="p989mcpsimp"></a><a name="p989mcpsimp"></a>src_phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p991mcpsimp"><a name="p991mcpsimp"></a><a name="p991mcpsimp"></a>源数据（待解密的数据）的物理地址。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p993mcpsimp"><a name="p993mcpsimp"></a><a name="p993mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row994mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p996mcpsimp"><a name="p996mcpsimp"></a><a name="p996mcpsimp"></a>dst_phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p998mcpsimp"><a name="p998mcpsimp"></a><a name="p998mcpsimp"></a>存放解密结果的物理地址。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1000mcpsimp"><a name="p1000mcpsimp"></a><a name="p1000mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1001mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1003mcpsimp"><a name="p1003mcpsimp"></a><a name="p1003mcpsimp"></a>byte_len</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1005mcpsimp"><a name="p1005mcpsimp"></a><a name="p1005mcpsimp"></a>数据的长度（单位：byte）。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1007mcpsimp"><a name="p1007mcpsimp"></a><a name="p1007mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1009mcpsimp"></a>
<table><thead align="left"><tr id="row1014mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1016mcpsimp"><a name="p1016mcpsimp"></a><a name="p1016mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1018mcpsimp"><a name="p1018mcpsimp"></a><a name="p1018mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1020mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1022mcpsimp"><a name="p1022mcpsimp"></a><a name="p1022mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1024mcpsimp"><a name="p1024mcpsimp"></a><a name="p1024mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1025mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1027mcpsimp"><a name="p1027mcpsimp"></a><a name="p1027mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1029mcpsimp"><a name="p1029mcpsimp"></a><a name="p1029mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   可多次调用，需配合  [ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)  使用，使用方法可参考  [注意事项](#ZH-CN_TOPIC_0000002441653065)。
-   模式为CTR/CCM/GCM时数据的长度为任意长度，其他模式要求block对齐。
-   解密的源地址、目的地址可以相同。
-   optee平台不支持。

【举例】

无。

## ss\_mpi\_cipher\_encrypt\_virt<a name="ZH-CN_TOPIC_0000002408253614"></a>

【描述】

对称加解密时对虚拟内存数据进行加密。

【语法】

```
td_s32 ss_mpi_cipher_encrypt_virt(td_handle handle, const td_u8 *src_data, td_u8 *dst_data, td_u32 byte_len);
```

【参数】

<a name="table1050mcpsimp"></a>
<table><thead align="left"><tr id="row1056mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p1058mcpsimp"><a name="p1058mcpsimp"></a><a name="p1058mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p1060mcpsimp"><a name="p1060mcpsimp"></a><a name="p1060mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1062mcpsimp"><a name="p1062mcpsimp"></a><a name="p1062mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1064mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1066mcpsimp"><a name="p1066mcpsimp"></a><a name="p1066mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1068mcpsimp"><a name="p1068mcpsimp"></a><a name="p1068mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1070mcpsimp"><a name="p1070mcpsimp"></a><a name="p1070mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1071mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1073mcpsimp"><a name="p1073mcpsimp"></a><a name="p1073mcpsimp"></a>src_data</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1075mcpsimp"><a name="p1075mcpsimp"></a><a name="p1075mcpsimp"></a>源数据（待加密的数据）的虚拟地址。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1077mcpsimp"><a name="p1077mcpsimp"></a><a name="p1077mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1078mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1080mcpsimp"><a name="p1080mcpsimp"></a><a name="p1080mcpsimp"></a>dst_data</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1082mcpsimp"><a name="p1082mcpsimp"></a><a name="p1082mcpsimp"></a>存放加密结果的虚拟地址。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1084mcpsimp"><a name="p1084mcpsimp"></a><a name="p1084mcpsimp"></a>输出</p>
</td>
</tr>
<tr id="row1085mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1087mcpsimp"><a name="p1087mcpsimp"></a><a name="p1087mcpsimp"></a>byte_len</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1089mcpsimp"><a name="p1089mcpsimp"></a><a name="p1089mcpsimp"></a>数据的长度（单位：byte）。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1091mcpsimp"><a name="p1091mcpsimp"></a><a name="p1091mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1093mcpsimp"></a>
<table><thead align="left"><tr id="row1098mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1100mcpsimp"><a name="p1100mcpsimp"></a><a name="p1100mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1102mcpsimp"><a name="p1102mcpsimp"></a><a name="p1102mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1104mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1106mcpsimp"><a name="p1106mcpsimp"></a><a name="p1106mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1108mcpsimp"><a name="p1108mcpsimp"></a><a name="p1108mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1109mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1111mcpsimp"><a name="p1111mcpsimp"></a><a name="p1111mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1113mcpsimp"><a name="p1113mcpsimp"></a><a name="p1113mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   可多次调用，需配合   [ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)  使用，使用方法可参考“[注意事项](#ZH-CN_TOPIC_0000002441653065)” 。
-   模式为CTR/CCM/GCM时数据的长度为任意长度，其他模式要求block对齐。
-   加密的源地址、目的地址可以相同。
-   一次加密的数据长度byte\_len最大不能超过4M。

【举例】

无。

## ss\_mpi\_cipher\_decrypt\_virt<a name="ZH-CN_TOPIC_0000002441572833"></a>

【描述】

对称加解密时对虚拟内存数据进行解密。

【语法】

```
td_s32 ss_mpi_cipher_decrypt_virt(td_handle handle, const td_u8 *src_data, td_u8 *dst_data, td_u32 byte_len);
```

【参数】

<a name="table1134mcpsimp"></a>
<table><thead align="left"><tr id="row1140mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p1142mcpsimp"><a name="p1142mcpsimp"></a><a name="p1142mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p1144mcpsimp"><a name="p1144mcpsimp"></a><a name="p1144mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1146mcpsimp"><a name="p1146mcpsimp"></a><a name="p1146mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1148mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1150mcpsimp"><a name="p1150mcpsimp"></a><a name="p1150mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1152mcpsimp"><a name="p1152mcpsimp"></a><a name="p1152mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1154mcpsimp"><a name="p1154mcpsimp"></a><a name="p1154mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1155mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1157mcpsimp"><a name="p1157mcpsimp"></a><a name="p1157mcpsimp"></a>src_data</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1159mcpsimp"><a name="p1159mcpsimp"></a><a name="p1159mcpsimp"></a>源数据（待解密的数据）的虚拟地址。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1161mcpsimp"><a name="p1161mcpsimp"></a><a name="p1161mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1162mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1164mcpsimp"><a name="p1164mcpsimp"></a><a name="p1164mcpsimp"></a>dst_data</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1166mcpsimp"><a name="p1166mcpsimp"></a><a name="p1166mcpsimp"></a>存放解密结果的虚拟地址。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1168mcpsimp"><a name="p1168mcpsimp"></a><a name="p1168mcpsimp"></a>输出</p>
</td>
</tr>
<tr id="row1169mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1171mcpsimp"><a name="p1171mcpsimp"></a><a name="p1171mcpsimp"></a>byte_len</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1173mcpsimp"><a name="p1173mcpsimp"></a><a name="p1173mcpsimp"></a>数据的长度（单位：byte）。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1175mcpsimp"><a name="p1175mcpsimp"></a><a name="p1175mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1177mcpsimp"></a>
<table><thead align="left"><tr id="row1182mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1184mcpsimp"><a name="p1184mcpsimp"></a><a name="p1184mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1186mcpsimp"><a name="p1186mcpsimp"></a><a name="p1186mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1188mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1190mcpsimp"><a name="p1190mcpsimp"></a><a name="p1190mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1192mcpsimp"><a name="p1192mcpsimp"></a><a name="p1192mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1193mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1195mcpsimp"><a name="p1195mcpsimp"></a><a name="p1195mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1197mcpsimp"><a name="p1197mcpsimp"></a><a name="p1197mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   可多次调用，需配合[ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)  使用，使用方法可参考“[注意事项](#ZH-CN_TOPIC_0000002441653065)” 。
-   模式为CTR/CCM/GCM时数据的长度为任意长度，其他模式要求block对齐。
-   解密的源地址、目的地址可以相同。
-   一次解密的数据长度byte\_len最大不能超过4M。

【举例】

无。

## ss\_mpi\_cipher\_encrypt\_multi\_pack<a name="ZH-CN_TOPIC_0000002408093690"></a>

【描述】

对称加解密时进行多个包数据的加密。

【语法】

```
td_s32 ss_mpi_cipher_encrypt_multi_pack(td_handle handle, const ot_cipher_data *data_pack,
td_u32 data_pack_num);
```

【参数】

<a name="table1220mcpsimp"></a>
<table><thead align="left"><tr id="row1226mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p1228mcpsimp"><a name="p1228mcpsimp"></a><a name="p1228mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.2"><p id="p1230mcpsimp"><a name="p1230mcpsimp"></a><a name="p1230mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1232mcpsimp"><a name="p1232mcpsimp"></a><a name="p1232mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1234mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1236mcpsimp"><a name="p1236mcpsimp"></a><a name="p1236mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1238mcpsimp"><a name="p1238mcpsimp"></a><a name="p1238mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1240mcpsimp"><a name="p1240mcpsimp"></a><a name="p1240mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1241mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1243mcpsimp"><a name="p1243mcpsimp"></a><a name="p1243mcpsimp"></a>data_pack</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1245mcpsimp"><a name="p1245mcpsimp"></a><a name="p1245mcpsimp"></a>待加密的数据包。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1247mcpsimp"><a name="p1247mcpsimp"></a><a name="p1247mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1248mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1250mcpsimp"><a name="p1250mcpsimp"></a><a name="p1250mcpsimp"></a>data_pack_num</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1252mcpsimp"><a name="p1252mcpsimp"></a><a name="p1252mcpsimp"></a>待加密的数据包个数。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1254mcpsimp"><a name="p1254mcpsimp"></a><a name="p1254mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1256mcpsimp"></a>
<table><thead align="left"><tr id="row1261mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1263mcpsimp"><a name="p1263mcpsimp"></a><a name="p1263mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1265mcpsimp"><a name="p1265mcpsimp"></a><a name="p1265mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1267mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1269mcpsimp"><a name="p1269mcpsimp"></a><a name="p1269mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1271mcpsimp"><a name="p1271mcpsimp"></a><a name="p1271mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1272mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1274mcpsimp"><a name="p1274mcpsimp"></a><a name="p1274mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1276mcpsimp"><a name="p1276mcpsimp"></a><a name="p1276mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   可多次调用，需配合  [ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)使用，使用方法可参考 “[注意事项](#ZH-CN_TOPIC_0000002441653065)”。
-   对于多个包的操作，每个包都使用[ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)配置的向量进行运算，前一个包的向量运算结果不会作用于下一个包的运算，每个包都是独立运算的。前一次函数调用的结果也不会影响后一次函数调用的运算结果。
-   加密的源地址、目的地址可以相同。
-   data\_pack\_num取值范围为1\~5000。
-   optee平台不支持。

【举例】

无。

## ss\_mpi\_cipher\_decrypt\_multi\_pack<a name="ZH-CN_TOPIC_0000002441653025"></a>

【描述】

对称加解密时进行多个包数据的解密。

【语法】

```
td_s32 ss_mpi_cipher_decrypt_multi_pack(td_handle handle, const ot_cipher_data *data_pack, td_u32 data_pack_num);
```

【参数】

<a name="table1301mcpsimp"></a>
<table><thead align="left"><tr id="row1307mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p1309mcpsimp"><a name="p1309mcpsimp"></a><a name="p1309mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.4.1.2"><p id="p1311mcpsimp"><a name="p1311mcpsimp"></a><a name="p1311mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1313mcpsimp"><a name="p1313mcpsimp"></a><a name="p1313mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1315mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p1317mcpsimp"><a name="p1317mcpsimp"></a><a name="p1317mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p1319mcpsimp"><a name="p1319mcpsimp"></a><a name="p1319mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1321mcpsimp"><a name="p1321mcpsimp"></a><a name="p1321mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1322mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p1324mcpsimp"><a name="p1324mcpsimp"></a><a name="p1324mcpsimp"></a>data_pack</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p1326mcpsimp"><a name="p1326mcpsimp"></a><a name="p1326mcpsimp"></a>待解密的数据包。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1328mcpsimp"><a name="p1328mcpsimp"></a><a name="p1328mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1329mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p1331mcpsimp"><a name="p1331mcpsimp"></a><a name="p1331mcpsimp"></a>data_pack_num</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p1333mcpsimp"><a name="p1333mcpsimp"></a><a name="p1333mcpsimp"></a>待解密的数据包个数。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1335mcpsimp"><a name="p1335mcpsimp"></a><a name="p1335mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1337mcpsimp"></a>
<table><thead align="left"><tr id="row1342mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1344mcpsimp"><a name="p1344mcpsimp"></a><a name="p1344mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1346mcpsimp"><a name="p1346mcpsimp"></a><a name="p1346mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1348mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1350mcpsimp"><a name="p1350mcpsimp"></a><a name="p1350mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1352mcpsimp"><a name="p1352mcpsimp"></a><a name="p1352mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1353mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1355mcpsimp"><a name="p1355mcpsimp"></a><a name="p1355mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1357mcpsimp"><a name="p1357mcpsimp"></a><a name="p1357mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   可多次调用，需配合  [ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)  使用，使用方法可参考 “[注意事项](#ZH-CN_TOPIC_0000002441653065)”。
-   对于多个包的操作，每个包都使用[ss\_mpi\_cipher\_set\_cfg](#ZH-CN_TOPIC_0000002408253622)配置的向量进行运算，前一个包的向量运算结果不会作用于下一个包的运算，每个包都是独立运算的。前一次函数调用的结果也不会影响后一次函数调用的运算结果。
-   解密的源地址、目的地址可以相同。
-   data\_pack\_num取值范围为1\~5000。
-   optee平台不支持。

【举例】

无。

## ss\_mpi\_cipher\_get\_tag<a name="ZH-CN_TOPIC_0000002441653053"></a>

【描述】

对称加解密时CCM/GCM模式获取TAG值。

【语法】

```
td_s32 ss_mpi_cipher_get_tag(td_handle handle, td_u8 *tag, td_u32 tag_len);
```

【参数】

<a name="table1379mcpsimp"></a>
<table><thead align="left"><tr id="row1385mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p1387mcpsimp"><a name="p1387mcpsimp"></a><a name="p1387mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.2"><p id="p1389mcpsimp"><a name="p1389mcpsimp"></a><a name="p1389mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1391mcpsimp"><a name="p1391mcpsimp"></a><a name="p1391mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1393mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1395mcpsimp"><a name="p1395mcpsimp"></a><a name="p1395mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1397mcpsimp"><a name="p1397mcpsimp"></a><a name="p1397mcpsimp"></a>CIPHER句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1399mcpsimp"><a name="p1399mcpsimp"></a><a name="p1399mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1400mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1402mcpsimp"><a name="p1402mcpsimp"></a><a name="p1402mcpsimp"></a>tag</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1404mcpsimp"><a name="p1404mcpsimp"></a><a name="p1404mcpsimp"></a>TAG值。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1406mcpsimp"><a name="p1406mcpsimp"></a><a name="p1406mcpsimp"></a>输出</p>
</td>
</tr>
<tr id="row1407mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1409mcpsimp"><a name="p1409mcpsimp"></a><a name="p1409mcpsimp"></a>tag_len</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1411mcpsimp"><a name="p1411mcpsimp"></a><a name="p1411mcpsimp"></a>TAG的输入缓冲区的大小（单位：byte）。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1413mcpsimp"><a name="p1413mcpsimp"></a><a name="p1413mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1415mcpsimp"></a>
<table><thead align="left"><tr id="row1420mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1422mcpsimp"><a name="p1422mcpsimp"></a><a name="p1422mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1424mcpsimp"><a name="p1424mcpsimp"></a><a name="p1424mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1426mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1428mcpsimp"><a name="p1428mcpsimp"></a><a name="p1428mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1430mcpsimp"><a name="p1430mcpsimp"></a><a name="p1430mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1431mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1433mcpsimp"><a name="p1433mcpsimp"></a><a name="p1433mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1435mcpsimp"><a name="p1435mcpsimp"></a><a name="p1435mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   CIPHER句柄必须已创建。
-   tag不能为空。
-   输入tag\_len小于[ot\_cipher\_ctrl\_aes\_ccm\_gcm](#ZH-CN_TOPIC_0000002441572857)结构体成员tag\_len指定的值时，接口异常。
-   只有在CCM、GCM模式下此接口才有效。

【举例】

无。

## ss\_mpi\_cipher\_hash\_init<a name="ZH-CN_TOPIC_0000002408093678"></a>

【描述】

初始化HASH模块。

【语法】

```
td_s32 ss_mpi_cipher_hash_init(const ot_cipher_hash_attr *hash_attr, td_handle *handle);
```

【参数】

<a name="table1458mcpsimp"></a>
<table><thead align="left"><tr id="row1464mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p1466mcpsimp"><a name="p1466mcpsimp"></a><a name="p1466mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.2"><p id="p1468mcpsimp"><a name="p1468mcpsimp"></a><a name="p1468mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1470mcpsimp"><a name="p1470mcpsimp"></a><a name="p1470mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1472mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1474mcpsimp"><a name="p1474mcpsimp"></a><a name="p1474mcpsimp"></a>hash_attr</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1476mcpsimp"><a name="p1476mcpsimp"></a><a name="p1476mcpsimp"></a>用于计算HASH的结构体参数。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1478mcpsimp"><a name="p1478mcpsimp"></a><a name="p1478mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1479mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1481mcpsimp"><a name="p1481mcpsimp"></a><a name="p1481mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1483mcpsimp"><a name="p1483mcpsimp"></a><a name="p1483mcpsimp"></a>输出的HASH句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1485mcpsimp"><a name="p1485mcpsimp"></a><a name="p1485mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1487mcpsimp"></a>
<table><thead align="left"><tr id="row1492mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1494mcpsimp"><a name="p1494mcpsimp"></a><a name="p1494mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1496mcpsimp"><a name="p1496mcpsimp"></a><a name="p1496mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1498mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1500mcpsimp"><a name="p1500mcpsimp"></a><a name="p1500mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1502mcpsimp"><a name="p1502mcpsimp"></a><a name="p1502mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1503mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1505mcpsimp"><a name="p1505mcpsimp"></a><a name="p1505mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1507mcpsimp"><a name="p1507mcpsimp"></a><a name="p1507mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   hash\_attr，handle不能为空。
-   如果有其他程序正在使用HASH模块，返回失败状态。

【举例】

无。

## ss\_mpi\_cipher\_hash\_update<a name="ZH-CN_TOPIC_0000002408253598"></a>

【描述】

计算hash值。

【语法】

```
td_s32 ss_mpi_cipher_hash_update(td_handle handle, const td_u8 *in_data, td_u32 in_data_len);
```

【参数】

<a name="table1525mcpsimp"></a>
<table><thead align="left"><tr id="row1531mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p1533mcpsimp"><a name="p1533mcpsimp"></a><a name="p1533mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.2"><p id="p1535mcpsimp"><a name="p1535mcpsimp"></a><a name="p1535mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1537mcpsimp"><a name="p1537mcpsimp"></a><a name="p1537mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1539mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1541mcpsimp"><a name="p1541mcpsimp"></a><a name="p1541mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1543mcpsimp"><a name="p1543mcpsimp"></a><a name="p1543mcpsimp"></a>HASH句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1545mcpsimp"><a name="p1545mcpsimp"></a><a name="p1545mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1546mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1548mcpsimp"><a name="p1548mcpsimp"></a><a name="p1548mcpsimp"></a>in_data</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1550mcpsimp"><a name="p1550mcpsimp"></a><a name="p1550mcpsimp"></a>输入数据。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1552mcpsimp"><a name="p1552mcpsimp"></a><a name="p1552mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1553mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1555mcpsimp"><a name="p1555mcpsimp"></a><a name="p1555mcpsimp"></a>in_data_len</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1557mcpsimp"><a name="p1557mcpsimp"></a><a name="p1557mcpsimp"></a>输入数据的长度，单位：byte。</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1559mcpsimp"><a name="p1559mcpsimp"></a><a name="p1559mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1561mcpsimp"></a>
<table><thead align="left"><tr id="row1566mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1568mcpsimp"><a name="p1568mcpsimp"></a><a name="p1568mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1570mcpsimp"><a name="p1570mcpsimp"></a><a name="p1570mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1572mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1574mcpsimp"><a name="p1574mcpsimp"></a><a name="p1574mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1576mcpsimp"><a name="p1576mcpsimp"></a><a name="p1576mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1577mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1579mcpsimp"><a name="p1579mcpsimp"></a><a name="p1579mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1581mcpsimp"><a name="p1581mcpsimp"></a><a name="p1581mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   Hash句柄必须已经创建。
-   可以分多次调用，每次计算若干个block。

【举例】

无。

## ss\_mpi\_cipher\_hash\_final<a name="ZH-CN_TOPIC_0000002408093722"></a>

【描述】

获取hash值。

【语法】

```
td_s32 ss_mpi_cipher_hash_final(td_handle handle, td_u8 *out_hash, td_u32 out_hash_len);
```

【参数】

<a name="table1601mcpsimp"></a>
<table><thead align="left"><tr id="row1607mcpsimp"><th class="cellrowborder" valign="top" width="24%" id="mcps1.1.4.1.1"><p id="p1609mcpsimp"><a name="p1609mcpsimp"></a><a name="p1609mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.2"><p id="p1611mcpsimp"><a name="p1611mcpsimp"></a><a name="p1611mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="16%" id="mcps1.1.4.1.3"><p id="p1613mcpsimp"><a name="p1613mcpsimp"></a><a name="p1613mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1615mcpsimp"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1617mcpsimp"><a name="p1617mcpsimp"></a><a name="p1617mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1619mcpsimp"><a name="p1619mcpsimp"></a><a name="p1619mcpsimp"></a>HASH句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p1621mcpsimp"><a name="p1621mcpsimp"></a><a name="p1621mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1622mcpsimp"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1624mcpsimp"><a name="p1624mcpsimp"></a><a name="p1624mcpsimp"></a>out_hash</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1626mcpsimp"><a name="p1626mcpsimp"></a><a name="p1626mcpsimp"></a>输出的HASH值。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p1628mcpsimp"><a name="p1628mcpsimp"></a><a name="p1628mcpsimp"></a>输出</p>
</td>
</tr>
<tr id="row1629mcpsimp"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.1.4.1.1 "><p id="p1631mcpsimp"><a name="p1631mcpsimp"></a><a name="p1631mcpsimp"></a>out_hash_len</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1633mcpsimp"><a name="p1633mcpsimp"></a><a name="p1633mcpsimp"></a>输出的HASH缓冲区长度，单位：byte。</p>
</td>
<td class="cellrowborder" valign="top" width="16%" headers="mcps1.1.4.1.3 "><p id="p1635mcpsimp"><a name="p1635mcpsimp"></a><a name="p1635mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1637mcpsimp"></a>
<table><thead align="left"><tr id="row1642mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1644mcpsimp"><a name="p1644mcpsimp"></a><a name="p1644mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1646mcpsimp"><a name="p1646mcpsimp"></a><a name="p1646mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1648mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1650mcpsimp"><a name="p1650mcpsimp"></a><a name="p1650mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1652mcpsimp"><a name="p1652mcpsimp"></a><a name="p1652mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1653mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1655mcpsimp"><a name="p1655mcpsimp"></a><a name="p1655mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1657mcpsimp"><a name="p1657mcpsimp"></a><a name="p1657mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

out\_hash\_len不能小于指定hash的输出长度。sha256输出长度为32byte，sha384输出长度为48byte，sha512输出长度为64byte，sm3输出长度为32byte。

【举例】

无。

## ss\_mpi\_cipher\_get\_random\_num<a name="ZH-CN_TOPIC_0000002408253630"></a>

【描述】

生成随机数。

【语法】

```
td_s32 ss_mpi_cipher_get_random_num(td_u32 *random_num);
```

【参数】

<a name="table1673mcpsimp"></a>
<table><thead align="left"><tr id="row1679mcpsimp"><th class="cellrowborder" valign="top" width="28.71%" id="mcps1.1.4.1.1"><p id="p1681mcpsimp"><a name="p1681mcpsimp"></a><a name="p1681mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="51.49%" id="mcps1.1.4.1.2"><p id="p1683mcpsimp"><a name="p1683mcpsimp"></a><a name="p1683mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="19.8%" id="mcps1.1.4.1.3"><p id="p1685mcpsimp"><a name="p1685mcpsimp"></a><a name="p1685mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1687mcpsimp"><td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.1.4.1.1 "><p id="p1689mcpsimp"><a name="p1689mcpsimp"></a><a name="p1689mcpsimp"></a>random_num</p>
</td>
<td class="cellrowborder" valign="top" width="51.49%" headers="mcps1.1.4.1.2 "><p id="p1691mcpsimp"><a name="p1691mcpsimp"></a><a name="p1691mcpsimp"></a>输出的随机数。</p>
</td>
<td class="cellrowborder" valign="top" width="19.8%" headers="mcps1.1.4.1.3 "><p id="p1693mcpsimp"><a name="p1693mcpsimp"></a><a name="p1693mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1695mcpsimp"></a>
<table><thead align="left"><tr id="row1700mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1702mcpsimp"><a name="p1702mcpsimp"></a><a name="p1702mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1704mcpsimp"><a name="p1704mcpsimp"></a><a name="p1704mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1706mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1708mcpsimp"><a name="p1708mcpsimp"></a><a name="p1708mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1710mcpsimp"><a name="p1710mcpsimp"></a><a name="p1710mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1711mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1713mcpsimp"><a name="p1713mcpsimp"></a><a name="p1713mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1715mcpsimp"><a name="p1715mcpsimp"></a><a name="p1715mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

random\_num不能为空。

【举例】

无。

## ss\_mpi\_cipher\_rsa\_public\_encrypt<a name="ZH-CN_TOPIC_0000002408253586"></a>

【描述】

使用RSA公钥加密一段明文。

【语法】

```
td_s32 ss_mpi_cipher_rsa_public_encrypt(ot_cipher_rsa_scheme scheme, ot_cipher_hash_type sha_type, const ot_cipher_rsa_public_key *rsa_key,    const ot_cipher_common_data *plain_txt, ot_cipher_common_data*cipher_txt);
```

【参数】

<a name="table1740mcpsimp"></a>
<table><thead align="left"><tr id="row1746mcpsimp"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.1.4.1.1"><p id="p1748mcpsimp"><a name="p1748mcpsimp"></a><a name="p1748mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.1.4.1.2"><p id="p1750mcpsimp"><a name="p1750mcpsimp"></a><a name="p1750mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.4.1.3"><p id="p1752mcpsimp"><a name="p1752mcpsimp"></a><a name="p1752mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1754mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1756mcpsimp"><a name="p1756mcpsimp"></a><a name="p1756mcpsimp"></a>scheme</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p1758mcpsimp"><a name="p1758mcpsimp"></a><a name="p1758mcpsimp"></a>RSA填充方式<span xml:lang="en-US" id="ph1759mcpsimp"><a name="ph1759mcpsimp"></a><a name="ph1759mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1761mcpsimp"><a name="p1761mcpsimp"></a><a name="p1761mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1762mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1764mcpsimp"><a name="p1764mcpsimp"></a><a name="p1764mcpsimp"></a>sha_type</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p1766mcpsimp"><a name="p1766mcpsimp"></a><a name="p1766mcpsimp"></a>RSA使用的摘要算法。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1768mcpsimp"><a name="p1768mcpsimp"></a><a name="p1768mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1769mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1771mcpsimp"><a name="p1771mcpsimp"></a><a name="p1771mcpsimp"></a>rsa_key</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1773mcpsimp"><a name="p1773mcpsimp"></a><a name="p1773mcpsimp"></a>密钥结构体。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1775mcpsimp"><a name="p1775mcpsimp"></a><a name="p1775mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1776mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1778mcpsimp"><a name="p1778mcpsimp"></a><a name="p1778mcpsimp"></a>plain_txt</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1780mcpsimp"><a name="p1780mcpsimp"></a><a name="p1780mcpsimp"></a>明文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1782mcpsimp"><a name="p1782mcpsimp"></a><a name="p1782mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1783mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1785mcpsimp"><a name="p1785mcpsimp"></a><a name="p1785mcpsimp"></a>cipher_txt</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1787mcpsimp"><a name="p1787mcpsimp"></a><a name="p1787mcpsimp"></a>密文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1789mcpsimp"><a name="p1789mcpsimp"></a><a name="p1789mcpsimp"></a>输入/输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1791mcpsimp"></a>
<table><thead align="left"><tr id="row1796mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1798mcpsimp"><a name="p1798mcpsimp"></a><a name="p1798mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1800mcpsimp"><a name="p1800mcpsimp"></a><a name="p1800mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1802mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1804mcpsimp"><a name="p1804mcpsimp"></a><a name="p1804mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1806mcpsimp"><a name="p1806mcpsimp"></a><a name="p1806mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1807mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1809mcpsimp"><a name="p1809mcpsimp"></a><a name="p1809mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1811mcpsimp"><a name="p1811mcpsimp"></a><a name="p1811mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   rsa\_key，plain\_txt，cipher\_txt不能为空。
-   cipher\_txt的成员data\_len即是加密的数据缓冲区长度，也是加密输出的数据长度。缓冲区长度不能小于输出的数据长度。
-   RSA填充方式为OT\_CIPHER\_RSA\_SCHEME\_PKCS1\_V15时，sha\_type不影响加解密结果。

【举例】

无。

## ss\_mpi\_cipher\_rsa\_private\_decrypt<a name="ZH-CN_TOPIC_0000002408093710"></a>

【描述】

使用RSA私钥解密一段密文。

【语法】

```
td_s32 ss_mpi_cipher_rsa_private_decrypt(ot_cipher_rsa_scheme scheme, ot_cipher_hash_type sha_type, const ot_cipher_rsa_private_key *rsa_key, const ot_cipher_common_data *cipher_txt, ot_cipher_common_data*plain_txt);
```

【参数】

<a name="table1836mcpsimp"></a>
<table><thead align="left"><tr id="row1842mcpsimp"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.1.4.1.1"><p id="p1844mcpsimp"><a name="p1844mcpsimp"></a><a name="p1844mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.1.4.1.2"><p id="p1846mcpsimp"><a name="p1846mcpsimp"></a><a name="p1846mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.4.1.3"><p id="p1848mcpsimp"><a name="p1848mcpsimp"></a><a name="p1848mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1850mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1852mcpsimp"><a name="p1852mcpsimp"></a><a name="p1852mcpsimp"></a>scheme</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p1854mcpsimp"><a name="p1854mcpsimp"></a><a name="p1854mcpsimp"></a>RSA填充方式<span xml:lang="en-US" id="ph1855mcpsimp"><a name="ph1855mcpsimp"></a><a name="ph1855mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1857mcpsimp"><a name="p1857mcpsimp"></a><a name="p1857mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1858mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1860mcpsimp"><a name="p1860mcpsimp"></a><a name="p1860mcpsimp"></a>sha_type</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p1862mcpsimp"><a name="p1862mcpsimp"></a><a name="p1862mcpsimp"></a>RSA使用的摘要算法。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1864mcpsimp"><a name="p1864mcpsimp"></a><a name="p1864mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1865mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1867mcpsimp"><a name="p1867mcpsimp"></a><a name="p1867mcpsimp"></a>rsa_key</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1869mcpsimp"><a name="p1869mcpsimp"></a><a name="p1869mcpsimp"></a>密钥结构体。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1871mcpsimp"><a name="p1871mcpsimp"></a><a name="p1871mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1872mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1874mcpsimp"><a name="p1874mcpsimp"></a><a name="p1874mcpsimp"></a>cipher_txt</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1876mcpsimp"><a name="p1876mcpsimp"></a><a name="p1876mcpsimp"></a>密文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1878mcpsimp"><a name="p1878mcpsimp"></a><a name="p1878mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1879mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1881mcpsimp"><a name="p1881mcpsimp"></a><a name="p1881mcpsimp"></a>plain_txt</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1883mcpsimp"><a name="p1883mcpsimp"></a><a name="p1883mcpsimp"></a>明文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1885mcpsimp"><a name="p1885mcpsimp"></a><a name="p1885mcpsimp"></a>输入/输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1887mcpsimp"></a>
<table><thead align="left"><tr id="row1892mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1894mcpsimp"><a name="p1894mcpsimp"></a><a name="p1894mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1896mcpsimp"><a name="p1896mcpsimp"></a><a name="p1896mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1898mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1900mcpsimp"><a name="p1900mcpsimp"></a><a name="p1900mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1902mcpsimp"><a name="p1902mcpsimp"></a><a name="p1902mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1903mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1905mcpsimp"><a name="p1905mcpsimp"></a><a name="p1905mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1907mcpsimp"><a name="p1907mcpsimp"></a><a name="p1907mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   rsa\_key，plain\_txt，cipher\_txt不能为空。
-   plain\_txt的成员data\_len即是解密的数据缓冲区长度，也是解密输出的数据长度。缓冲区长度不能小于输出的数据长度。

【举例】

无。

## ss\_mpi\_cipher\_rsa\_private\_encrypt<a name="ZH-CN_TOPIC_0000002441653041"></a>

【描述】

使用RSA私钥加密一段明文。

【语法】

```
td_s32 ss_mpi_cipher_rsa_private_encrypt(ot_cipher_rsa_scheme scheme, ot_cipher_hash_type sha_type, const ot_cipher_rsa_private_key *rsa_key, const ot_cipher_common_data *plain_txt, ot_cipher_common_data *cipher_txt);
```

【参数】

<a name="table1932mcpsimp"></a>
<table><thead align="left"><tr id="row1938mcpsimp"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.1.4.1.1"><p id="p1940mcpsimp"><a name="p1940mcpsimp"></a><a name="p1940mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="58.589999999999996%" id="mcps1.1.4.1.2"><p id="p1942mcpsimp"><a name="p1942mcpsimp"></a><a name="p1942mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17.169999999999998%" id="mcps1.1.4.1.3"><p id="p1944mcpsimp"><a name="p1944mcpsimp"></a><a name="p1944mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row1946mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1948mcpsimp"><a name="p1948mcpsimp"></a><a name="p1948mcpsimp"></a>scheme</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p1950mcpsimp"><a name="p1950mcpsimp"></a><a name="p1950mcpsimp"></a>RSA填充方式<span xml:lang="en-US" id="ph1951mcpsimp"><a name="ph1951mcpsimp"></a><a name="ph1951mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1953mcpsimp"><a name="p1953mcpsimp"></a><a name="p1953mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1954mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1956mcpsimp"><a name="p1956mcpsimp"></a><a name="p1956mcpsimp"></a>sha_type</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p1958mcpsimp"><a name="p1958mcpsimp"></a><a name="p1958mcpsimp"></a>RSA使用的摘要算法。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1960mcpsimp"><a name="p1960mcpsimp"></a><a name="p1960mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1961mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1963mcpsimp"><a name="p1963mcpsimp"></a><a name="p1963mcpsimp"></a>rsa_key</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1965mcpsimp"><a name="p1965mcpsimp"></a><a name="p1965mcpsimp"></a>密钥结构体。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1967mcpsimp"><a name="p1967mcpsimp"></a><a name="p1967mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1968mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1970mcpsimp"><a name="p1970mcpsimp"></a><a name="p1970mcpsimp"></a>plain_txt</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1972mcpsimp"><a name="p1972mcpsimp"></a><a name="p1972mcpsimp"></a>明文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1974mcpsimp"><a name="p1974mcpsimp"></a><a name="p1974mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row1975mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p1977mcpsimp"><a name="p1977mcpsimp"></a><a name="p1977mcpsimp"></a>cipher_txt</p>
</td>
<td class="cellrowborder" valign="top" width="58.589999999999996%" headers="mcps1.1.4.1.2 "><p id="p1979mcpsimp"><a name="p1979mcpsimp"></a><a name="p1979mcpsimp"></a>密文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17.169999999999998%" headers="mcps1.1.4.1.3 "><p id="p1981mcpsimp"><a name="p1981mcpsimp"></a><a name="p1981mcpsimp"></a>输入/输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table1983mcpsimp"></a>
<table><thead align="left"><tr id="row1988mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1990mcpsimp"><a name="p1990mcpsimp"></a><a name="p1990mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1992mcpsimp"><a name="p1992mcpsimp"></a><a name="p1992mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row1994mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1996mcpsimp"><a name="p1996mcpsimp"></a><a name="p1996mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1998mcpsimp"><a name="p1998mcpsimp"></a><a name="p1998mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row1999mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2001mcpsimp"><a name="p2001mcpsimp"></a><a name="p2001mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2003mcpsimp"><a name="p2003mcpsimp"></a><a name="p2003mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   rsa\_key，plain\_txt，cipher\_txt不能为空。
-   cipher\_txt的成员data\_len即是加密的数据缓冲区长度，也是加密输出的数据长度。缓冲区长度不能小于输出的数据长度。

【举例】

无。

## ss\_mpi\_cipher\_rsa\_public\_decrypt<a name="ZH-CN_TOPIC_0000002408253566"></a>

【描述】

使用RSA公钥解密一段密文。

【语法】

```
td_s32 ss_mpi_cipher_rsa_public_decrypt(ot_cipher_rsa_scheme scheme, ot_cipher_hash_type sha_type, const ot_cipher_rsa_public_key *rsa_key, const ot_cipher_common_data *cipher_txt, ot_cipher_common_data *plain_txt);
```

【参数】

<a name="table2028mcpsimp"></a>
<table><thead align="left"><tr id="row2034mcpsimp"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.1.4.1.1"><p id="p2036mcpsimp"><a name="p2036mcpsimp"></a><a name="p2036mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.1.4.1.2"><p id="p2038mcpsimp"><a name="p2038mcpsimp"></a><a name="p2038mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="26.76%" id="mcps1.1.4.1.3"><p id="p2040mcpsimp"><a name="p2040mcpsimp"></a><a name="p2040mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2042mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2044mcpsimp"><a name="p2044mcpsimp"></a><a name="p2044mcpsimp"></a>scheme</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2046mcpsimp"><a name="p2046mcpsimp"></a><a name="p2046mcpsimp"></a>RSA填充方式。</p>
</td>
<td class="cellrowborder" valign="top" width="26.76%" headers="mcps1.1.4.1.3 "><p id="p2049mcpsimp"><a name="p2049mcpsimp"></a><a name="p2049mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2050mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2052mcpsimp"><a name="p2052mcpsimp"></a><a name="p2052mcpsimp"></a>sha_type</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2054mcpsimp"><a name="p2054mcpsimp"></a><a name="p2054mcpsimp"></a>RSA使用的摘要算法。</p>
</td>
<td class="cellrowborder" valign="top" width="26.76%" headers="mcps1.1.4.1.3 "><p id="p2056mcpsimp"><a name="p2056mcpsimp"></a><a name="p2056mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2057mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2059mcpsimp"><a name="p2059mcpsimp"></a><a name="p2059mcpsimp"></a>rsa_key</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.4.1.2 "><p id="p2061mcpsimp"><a name="p2061mcpsimp"></a><a name="p2061mcpsimp"></a>密钥结构体。</p>
</td>
<td class="cellrowborder" valign="top" width="26.76%" headers="mcps1.1.4.1.3 "><p id="p2063mcpsimp"><a name="p2063mcpsimp"></a><a name="p2063mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2064mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2066mcpsimp"><a name="p2066mcpsimp"></a><a name="p2066mcpsimp"></a>cipher_txt</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.4.1.2 "><p id="p2068mcpsimp"><a name="p2068mcpsimp"></a><a name="p2068mcpsimp"></a>密文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="26.76%" headers="mcps1.1.4.1.3 "><p id="p2070mcpsimp"><a name="p2070mcpsimp"></a><a name="p2070mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2071mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2073mcpsimp"><a name="p2073mcpsimp"></a><a name="p2073mcpsimp"></a>plain_txt</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.4.1.2 "><p id="p2075mcpsimp"><a name="p2075mcpsimp"></a><a name="p2075mcpsimp"></a>明文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="26.76%" headers="mcps1.1.4.1.3 "><p id="p2077mcpsimp"><a name="p2077mcpsimp"></a><a name="p2077mcpsimp"></a>输入/输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2079mcpsimp"></a>
<table><thead align="left"><tr id="row2084mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2086mcpsimp"><a name="p2086mcpsimp"></a><a name="p2086mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2088mcpsimp"><a name="p2088mcpsimp"></a><a name="p2088mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2090mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2092mcpsimp"><a name="p2092mcpsimp"></a><a name="p2092mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2094mcpsimp"><a name="p2094mcpsimp"></a><a name="p2094mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2095mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2097mcpsimp"><a name="p2097mcpsimp"></a><a name="p2097mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2099mcpsimp"><a name="p2099mcpsimp"></a><a name="p2099mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   rsa\_key，plain\_txt，cipher\_txt不能为空。
-   plain\_txt的成员data\_len即是解密的数据缓冲区长度，也是解密输出的数据长度。缓冲区长度不能小于输出的数据长度。

【举例】

无。

## ss\_mpi\_cipher\_rsa\_sign<a name="ZH-CN_TOPIC_0000002441653009"></a>

【描述】

使用RSA私钥签名一段文本。

【语法】

```
td_s32 ss_mpi_cipher_rsa_sign(ot_cipher_rsa_scheme scheme, ot_cipher_hash_type sha_type, const ot_cipher_rsa_private_key *rsa_key, const ot_cipher_sign_in_data *rsa_data, ot_cipher_common_data *sign_data);
```

【参数】

<a name="table2124mcpsimp"></a>
<table><thead align="left"><tr id="row2130mcpsimp"><th class="cellrowborder" valign="top" width="24.240000000000002%" id="mcps1.1.4.1.1"><p id="p2132mcpsimp"><a name="p2132mcpsimp"></a><a name="p2132mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="49.76%" id="mcps1.1.4.1.2"><p id="p2134mcpsimp"><a name="p2134mcpsimp"></a><a name="p2134mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.3"><p id="p2136mcpsimp"><a name="p2136mcpsimp"></a><a name="p2136mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2138mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2140mcpsimp"><a name="p2140mcpsimp"></a><a name="p2140mcpsimp"></a>scheme</p>
</td>
<td class="cellrowborder" valign="top" width="49.76%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2142mcpsimp"><a name="p2142mcpsimp"></a><a name="p2142mcpsimp"></a>RSA填充方式<span xml:lang="en-US" id="ph2143mcpsimp"><a name="ph2143mcpsimp"></a><a name="ph2143mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.3 "><p id="p2145mcpsimp"><a name="p2145mcpsimp"></a><a name="p2145mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2146mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2148mcpsimp"><a name="p2148mcpsimp"></a><a name="p2148mcpsimp"></a>sha_type</p>
</td>
<td class="cellrowborder" valign="top" width="49.76%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2150mcpsimp"><a name="p2150mcpsimp"></a><a name="p2150mcpsimp"></a>RSA使用的摘要算法。</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.3 "><p id="p2152mcpsimp"><a name="p2152mcpsimp"></a><a name="p2152mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2153mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2155mcpsimp"><a name="p2155mcpsimp"></a><a name="p2155mcpsimp"></a>rsa_key</p>
</td>
<td class="cellrowborder" valign="top" width="49.76%" headers="mcps1.1.4.1.2 "><p id="p2157mcpsimp"><a name="p2157mcpsimp"></a><a name="p2157mcpsimp"></a>密钥结构体。</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.3 "><p id="p2159mcpsimp"><a name="p2159mcpsimp"></a><a name="p2159mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2160mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2162mcpsimp"><a name="p2162mcpsimp"></a><a name="p2162mcpsimp"></a>rsa_data</p>
</td>
<td class="cellrowborder" valign="top" width="49.76%" headers="mcps1.1.4.1.2 "><p id="p2164mcpsimp"><a name="p2164mcpsimp"></a><a name="p2164mcpsimp"></a>RSA签名输入的数据。</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.3 "><p id="p2166mcpsimp"><a name="p2166mcpsimp"></a><a name="p2166mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2167mcpsimp"><td class="cellrowborder" valign="top" width="24.240000000000002%" headers="mcps1.1.4.1.1 "><p id="p2169mcpsimp"><a name="p2169mcpsimp"></a><a name="p2169mcpsimp"></a>sign_data</p>
</td>
<td class="cellrowborder" valign="top" width="49.76%" headers="mcps1.1.4.1.2 "><p id="p2171mcpsimp"><a name="p2171mcpsimp"></a><a name="p2171mcpsimp"></a>RSA签名后的数据。</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.3 "><p id="p2173mcpsimp"><a name="p2173mcpsimp"></a><a name="p2173mcpsimp"></a>输入/输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2175mcpsimp"></a>
<table><thead align="left"><tr id="row2180mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2182mcpsimp"><a name="p2182mcpsimp"></a><a name="p2182mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2184mcpsimp"><a name="p2184mcpsimp"></a><a name="p2184mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2186mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2188mcpsimp"><a name="p2188mcpsimp"></a><a name="p2188mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2190mcpsimp"><a name="p2190mcpsimp"></a><a name="p2190mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2191mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2193mcpsimp"><a name="p2193mcpsimp"></a><a name="p2193mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2195mcpsimp"><a name="p2195mcpsimp"></a><a name="p2195mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   rsa\_key，rsa\_data，sign\_data不能为空。
-   sign\_data的成员data\_len即是签名的数据缓冲区长度，也是签名输出的数据长度。缓冲区长度不能小于输出的数据长度。

【举例】

无。

## ss\_mpi\_cipher\_rsa\_verify<a name="ZH-CN_TOPIC_0000002408253618"></a>

【描述】

使用RSA公钥验证一段文本。

【语法】

```
td_s32 ss_mpi_cipher_rsa_verify(ot_cipher_rsa_scheme scheme, ot_cipher_hash_type sha_type, const ot_cipher_rsa_public_key *rsa_key, const ot_cipher_sign_in_data *rsa_data, const ot_cipher_common_data *sign_data);
```

【参数】

<a name="table2220mcpsimp"></a>
<table><thead align="left"><tr id="row2226mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2228mcpsimp"><a name="p2228mcpsimp"></a><a name="p2228mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2230mcpsimp"><a name="p2230mcpsimp"></a><a name="p2230mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2232mcpsimp"><a name="p2232mcpsimp"></a><a name="p2232mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2234mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2236mcpsimp"><a name="p2236mcpsimp"></a><a name="p2236mcpsimp"></a>scheme</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2238mcpsimp"><a name="p2238mcpsimp"></a><a name="p2238mcpsimp"></a>RSA填充方式<span xml:lang="en-US" id="ph2239mcpsimp"><a name="ph2239mcpsimp"></a><a name="ph2239mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2241mcpsimp"><a name="p2241mcpsimp"></a><a name="p2241mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2242mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2244mcpsimp"><a name="p2244mcpsimp"></a><a name="p2244mcpsimp"></a>sha_type</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2246mcpsimp"><a name="p2246mcpsimp"></a><a name="p2246mcpsimp"></a>RSA使用的摘要算法。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2248mcpsimp"><a name="p2248mcpsimp"></a><a name="p2248mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2249mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2251mcpsimp"><a name="p2251mcpsimp"></a><a name="p2251mcpsimp"></a>rsa_key</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2253mcpsimp"><a name="p2253mcpsimp"></a><a name="p2253mcpsimp"></a>密钥结构体。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2255mcpsimp"><a name="p2255mcpsimp"></a><a name="p2255mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2256mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2258mcpsimp"><a name="p2258mcpsimp"></a><a name="p2258mcpsimp"></a>rsa_data</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2260mcpsimp"><a name="p2260mcpsimp"></a><a name="p2260mcpsimp"></a>RSA签名输入的数据。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2262mcpsimp"><a name="p2262mcpsimp"></a><a name="p2262mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2263mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2265mcpsimp"><a name="p2265mcpsimp"></a><a name="p2265mcpsimp"></a>sign_data</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2267mcpsimp"><a name="p2267mcpsimp"></a><a name="p2267mcpsimp"></a>RSA签名后的数据。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2269mcpsimp"><a name="p2269mcpsimp"></a><a name="p2269mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2271mcpsimp"></a>
<table><thead align="left"><tr id="row2276mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2278mcpsimp"><a name="p2278mcpsimp"></a><a name="p2278mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2280mcpsimp"><a name="p2280mcpsimp"></a><a name="p2280mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2282mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2284mcpsimp"><a name="p2284mcpsimp"></a><a name="p2284mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2286mcpsimp"><a name="p2286mcpsimp"></a><a name="p2286mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2287mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2289mcpsimp"><a name="p2289mcpsimp"></a><a name="p2289mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2291mcpsimp"><a name="p2291mcpsimp"></a><a name="p2291mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   rsa\_key，rsa\_data，sign\_data不能为空。
-   sign\_data的成员data\_len必须与rsa\_key的n\_len保持一致。

【举例】

无。

## ss\_mpi\_cipher\_sm2\_encrypt<a name="ZH-CN_TOPIC_0000002441572901"></a>

【描述】

使用SM2公钥加密一段明文。

【语法】

```
td_s32 ss_mpi_cipher_sm2_encrypt(const ot_cipher_sm2_public_key *sm2_key, const ot_cipher_common_data *plain_txt, ot_cipher_common_data*cipher_txt);
```

【参数】

<a name="table2312mcpsimp"></a>
<table><thead align="left"><tr id="row2318mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2320mcpsimp"><a name="p2320mcpsimp"></a><a name="p2320mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2322mcpsimp"><a name="p2322mcpsimp"></a><a name="p2322mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2324mcpsimp"><a name="p2324mcpsimp"></a><a name="p2324mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2326mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2328mcpsimp"><a name="p2328mcpsimp"></a><a name="p2328mcpsimp"></a>sm2_key</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2330mcpsimp"><a name="p2330mcpsimp"></a><a name="p2330mcpsimp"></a>SM2公钥结构体<span xml:lang="en-US" id="ph2331mcpsimp"><a name="ph2331mcpsimp"></a><a name="ph2331mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2333mcpsimp"><a name="p2333mcpsimp"></a><a name="p2333mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2334mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2336mcpsimp"><a name="p2336mcpsimp"></a><a name="p2336mcpsimp"></a>plain_txt</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2338mcpsimp"><a name="p2338mcpsimp"></a><a name="p2338mcpsimp"></a>明文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2340mcpsimp"><a name="p2340mcpsimp"></a><a name="p2340mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2341mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2343mcpsimp"><a name="p2343mcpsimp"></a><a name="p2343mcpsimp"></a>cipher_txt</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2345mcpsimp"><a name="p2345mcpsimp"></a><a name="p2345mcpsimp"></a>密文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2347mcpsimp"><a name="p2347mcpsimp"></a><a name="p2347mcpsimp"></a>输入/输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2349mcpsimp"></a>
<table><thead align="left"><tr id="row2354mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2356mcpsimp"><a name="p2356mcpsimp"></a><a name="p2356mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2358mcpsimp"><a name="p2358mcpsimp"></a><a name="p2358mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2360mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2362mcpsimp"><a name="p2362mcpsimp"></a><a name="p2362mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2364mcpsimp"><a name="p2364mcpsimp"></a><a name="p2364mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2365mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2367mcpsimp"><a name="p2367mcpsimp"></a><a name="p2367mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2369mcpsimp"><a name="p2369mcpsimp"></a><a name="p2369mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   sm2\_key，plain\_txt，cipher\_txt不能为空。
-   cipher\_txt的成员data\_len即是加密的数据缓冲区长度，也是加密输出的数据长度。缓冲区长度不能小于输出的数据长度。
-   SS928V100、SS626V100不支持SM2接口。

【举例】

无。

## ss\_mpi\_cipher\_sm2\_decrypt<a name="ZH-CN_TOPIC_0000002441653061"></a>

【描述】

使用SM2私钥解密一段密文。

【语法】

```
td_s32 ss_mpi_cipher_sm2_decrypt(const ot_cipher_sm2_private_key *sm2_key, const ot_cipher_common_data *cipher_txt, ot_cipher_common_data*plain_txt);
```

【参数】

<a name="table2391mcpsimp"></a>
<table><thead align="left"><tr id="row2397mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2399mcpsimp"><a name="p2399mcpsimp"></a><a name="p2399mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2401mcpsimp"><a name="p2401mcpsimp"></a><a name="p2401mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2403mcpsimp"><a name="p2403mcpsimp"></a><a name="p2403mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2405mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2407mcpsimp"><a name="p2407mcpsimp"></a><a name="p2407mcpsimp"></a>sm2_key</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2409mcpsimp"><a name="p2409mcpsimp"></a><a name="p2409mcpsimp"></a>SM2私钥结构体<span xml:lang="en-US" id="ph2410mcpsimp"><a name="ph2410mcpsimp"></a><a name="ph2410mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2412mcpsimp"><a name="p2412mcpsimp"></a><a name="p2412mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2413mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2415mcpsimp"><a name="p2415mcpsimp"></a><a name="p2415mcpsimp"></a>cipher_txt</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2417mcpsimp"><a name="p2417mcpsimp"></a><a name="p2417mcpsimp"></a>密文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2419mcpsimp"><a name="p2419mcpsimp"></a><a name="p2419mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2420mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2422mcpsimp"><a name="p2422mcpsimp"></a><a name="p2422mcpsimp"></a>plain_txt</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2424mcpsimp"><a name="p2424mcpsimp"></a><a name="p2424mcpsimp"></a>明文文本。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2426mcpsimp"><a name="p2426mcpsimp"></a><a name="p2426mcpsimp"></a>输入/输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2428mcpsimp"></a>
<table><thead align="left"><tr id="row2433mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2435mcpsimp"><a name="p2435mcpsimp"></a><a name="p2435mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2437mcpsimp"><a name="p2437mcpsimp"></a><a name="p2437mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2439mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2441mcpsimp"><a name="p2441mcpsimp"></a><a name="p2441mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2443mcpsimp"><a name="p2443mcpsimp"></a><a name="p2443mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2444mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2446mcpsimp"><a name="p2446mcpsimp"></a><a name="p2446mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2448mcpsimp"><a name="p2448mcpsimp"></a><a name="p2448mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   sm2\_key，plain\_txt，cipher\_txt不能为空。
-   plain\_txt的成员data\_len即是解密的数据缓冲区长度，也是解密输出的数据长度。缓冲区长度不能小于输出的数据长度。
-   SS928V100、SS626V100不支持SM2接口。

【举例】

无。

## ss\_mpi\_cipher\_sm2\_sign<a name="ZH-CN_TOPIC_0000002408253606"></a>

【描述】

使用SM2签名一段文本。

【语法】

```
td_s32 ss_mpi_cipher_sm2_sign(const ot_cipher_sm2_sign *sm2_sign, const ot_cipher_sign_in_data *sm2_data, ot_cipher_sm2_sign_data *sign_data);
```

【参数】

<a name="table2470mcpsimp"></a>
<table><thead align="left"><tr id="row2476mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2478mcpsimp"><a name="p2478mcpsimp"></a><a name="p2478mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2480mcpsimp"><a name="p2480mcpsimp"></a><a name="p2480mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2482mcpsimp"><a name="p2482mcpsimp"></a><a name="p2482mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2484mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2486mcpsimp"><a name="p2486mcpsimp"></a><a name="p2486mcpsimp"></a>sm2_sign</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2488mcpsimp"><a name="p2488mcpsimp"></a><a name="p2488mcpsimp"></a>SM2签名结构体<span xml:lang="en-US" id="ph2489mcpsimp"><a name="ph2489mcpsimp"></a><a name="ph2489mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2491mcpsimp"><a name="p2491mcpsimp"></a><a name="p2491mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2492mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2494mcpsimp"><a name="p2494mcpsimp"></a><a name="p2494mcpsimp"></a>sm2_data</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2496mcpsimp"><a name="p2496mcpsimp"></a><a name="p2496mcpsimp"></a>SM2签名输入的数据。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2498mcpsimp"><a name="p2498mcpsimp"></a><a name="p2498mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2499mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2501mcpsimp"><a name="p2501mcpsimp"></a><a name="p2501mcpsimp"></a>sign_data</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2503mcpsimp"><a name="p2503mcpsimp"></a><a name="p2503mcpsimp"></a>SM2签名后的数据。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2505mcpsimp"><a name="p2505mcpsimp"></a><a name="p2505mcpsimp"></a>输入/输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2507mcpsimp"></a>
<table><thead align="left"><tr id="row2512mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2514mcpsimp"><a name="p2514mcpsimp"></a><a name="p2514mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2516mcpsimp"><a name="p2516mcpsimp"></a><a name="p2516mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2518mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2520mcpsimp"><a name="p2520mcpsimp"></a><a name="p2520mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2522mcpsimp"><a name="p2522mcpsimp"></a><a name="p2522mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2523mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2525mcpsimp"><a name="p2525mcpsimp"></a><a name="p2525mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2527mcpsimp"><a name="p2527mcpsimp"></a><a name="p2527mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   sm2\_sign，sm2\_data，sign\_data不能为空。
-   当前SM2只支持签名数据类型OT\_CIPHER\_SIGN\_TYPE\_MSG。
-   SS928V100、SS626V100不支持SM2接口。

【举例】

无。

## ss\_mpi\_cipher\_sm2\_verify<a name="ZH-CN_TOPIC_0000002408093770"></a>

【描述】

使用SM2验证一段文本。

【语法】

```
td_s32 ss_mpi_cipher_sm2_verify(const ot_cipher_sm2_verify *sm2_verify, const ot_cipher_sign_in_data *sm2_data, const ot_cipher_sm2_sign_data*sign_data);
```

【参数】

<a name="table2549mcpsimp"></a>
<table><thead align="left"><tr id="row2555mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2557mcpsimp"><a name="p2557mcpsimp"></a><a name="p2557mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2559mcpsimp"><a name="p2559mcpsimp"></a><a name="p2559mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2561mcpsimp"><a name="p2561mcpsimp"></a><a name="p2561mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2563mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2565mcpsimp"><a name="p2565mcpsimp"></a><a name="p2565mcpsimp"></a>sm2_verify</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p xml:lang="de-DE" id="p2567mcpsimp"><a name="p2567mcpsimp"></a><a name="p2567mcpsimp"></a>SM2验签结构体<span xml:lang="en-US" id="ph2568mcpsimp"><a name="ph2568mcpsimp"></a><a name="ph2568mcpsimp"></a>。</span></p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2570mcpsimp"><a name="p2570mcpsimp"></a><a name="p2570mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2571mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2573mcpsimp"><a name="p2573mcpsimp"></a><a name="p2573mcpsimp"></a>sm2_data</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2575mcpsimp"><a name="p2575mcpsimp"></a><a name="p2575mcpsimp"></a>SM2签名输入的数据。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2577mcpsimp"><a name="p2577mcpsimp"></a><a name="p2577mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2578mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2580mcpsimp"><a name="p2580mcpsimp"></a><a name="p2580mcpsimp"></a>sign_data</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2582mcpsimp"><a name="p2582mcpsimp"></a><a name="p2582mcpsimp"></a>SM2签名后的数据。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2584mcpsimp"><a name="p2584mcpsimp"></a><a name="p2584mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2586mcpsimp"></a>
<table><thead align="left"><tr id="row2591mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2593mcpsimp"><a name="p2593mcpsimp"></a><a name="p2593mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2595mcpsimp"><a name="p2595mcpsimp"></a><a name="p2595mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2597mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2599mcpsimp"><a name="p2599mcpsimp"></a><a name="p2599mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2601mcpsimp"><a name="p2601mcpsimp"></a><a name="p2601mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2602mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2604mcpsimp"><a name="p2604mcpsimp"></a><a name="p2604mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2606mcpsimp"><a name="p2606mcpsimp"></a><a name="p2606mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   sm2\_verify，sm2\_data，sign\_data不能为空。
-   当前SM2只支持签名数据类型OT\_CIPHER\_SIGN\_TYPE\_MSG。
-   SS928V100、SS626V100不支持SM2接口。

【举例】

无。

## ss\_mpi\_keyslot\_create<a name="ZH-CN_TOPIC_0000002441572909"></a>

【描述】

对称加解密时创建的keyslot句柄。

【语法】

```
td_s32 ss_mpi_keyslot_create(const ot_keyslot_attr *attr, td_handle *keyslot);
```

【参数】

<a name="table2627mcpsimp"></a>
<table><thead align="left"><tr id="row2633mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2635mcpsimp"><a name="p2635mcpsimp"></a><a name="p2635mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2637mcpsimp"><a name="p2637mcpsimp"></a><a name="p2637mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2639mcpsimp"><a name="p2639mcpsimp"></a><a name="p2639mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2641mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2643mcpsimp"><a name="p2643mcpsimp"></a><a name="p2643mcpsimp"></a>attr</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2645mcpsimp"><a name="p2645mcpsimp"></a><a name="p2645mcpsimp"></a>keyslot属性结构体指针。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2647mcpsimp"><a name="p2647mcpsimp"></a><a name="p2647mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2648mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2650mcpsimp"><a name="p2650mcpsimp"></a><a name="p2650mcpsimp"></a>keyslot</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2652mcpsimp"><a name="p2652mcpsimp"></a><a name="p2652mcpsimp"></a>keyslot句柄指针。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2654mcpsimp"><a name="p2654mcpsimp"></a><a name="p2654mcpsimp"></a>输出</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2656mcpsimp"></a>
<table><thead align="left"><tr id="row2661mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2663mcpsimp"><a name="p2663mcpsimp"></a><a name="p2663mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2665mcpsimp"><a name="p2665mcpsimp"></a><a name="p2665mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2667mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2669mcpsimp"><a name="p2669mcpsimp"></a><a name="p2669mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2671mcpsimp"><a name="p2671mcpsimp"></a><a name="p2671mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2672mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2674mcpsimp"><a name="p2674mcpsimp"></a><a name="p2674mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2676mcpsimp"><a name="p2676mcpsimp"></a><a name="p2676mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   attr、keyslot不能为空。
-   使用完通道后，应销毁对应的通道。
-   最多可创建16个软件通道。

【举例】

无。

## ss\_mpi\_keyslot\_destroy<a name="ZH-CN_TOPIC_0000002408093686"></a>

【描述】

对称加解密时销毁的keyslot句柄。

【语法】

```
td_s32 ss_mpi_keyslot_destroy (td_handle keyslot);
```

【参数】

<a name="table2695mcpsimp"></a>
<table><thead align="left"><tr id="row2701mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2703mcpsimp"><a name="p2703mcpsimp"></a><a name="p2703mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2705mcpsimp"><a name="p2705mcpsimp"></a><a name="p2705mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2707mcpsimp"><a name="p2707mcpsimp"></a><a name="p2707mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2709mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2711mcpsimp"><a name="p2711mcpsimp"></a><a name="p2711mcpsimp"></a>keyslot</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2713mcpsimp"><a name="p2713mcpsimp"></a><a name="p2713mcpsimp"></a>keyslot句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2715mcpsimp"><a name="p2715mcpsimp"></a><a name="p2715mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2717mcpsimp"></a>
<table><thead align="left"><tr id="row2722mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2724mcpsimp"><a name="p2724mcpsimp"></a><a name="p2724mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2726mcpsimp"><a name="p2726mcpsimp"></a><a name="p2726mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2728mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2730mcpsimp"><a name="p2730mcpsimp"></a><a name="p2730mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2732mcpsimp"><a name="p2732mcpsimp"></a><a name="p2732mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2733mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2735mcpsimp"><a name="p2735mcpsimp"></a><a name="p2735mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2737mcpsimp"><a name="p2737mcpsimp"></a><a name="p2737mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   keyslot句柄必须已创建。
-   创建和销毁keyslot通道必须成对存在。

【举例】

无。

## ss\_mpi\_cipher\_attach<a name="ZH-CN_TOPIC_0000002408093718"></a>

【描述】

对称加解密时cipher句柄与keyslot句柄绑定。

【语法】

```
td_s32 ss_mpi_cipher_attach(td_handle cipher, td_handle keyslot);
```

【参数】

<a name="table2755mcpsimp"></a>
<table><thead align="left"><tr id="row2761mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2763mcpsimp"><a name="p2763mcpsimp"></a><a name="p2763mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2765mcpsimp"><a name="p2765mcpsimp"></a><a name="p2765mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2767mcpsimp"><a name="p2767mcpsimp"></a><a name="p2767mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2769mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2771mcpsimp"><a name="p2771mcpsimp"></a><a name="p2771mcpsimp"></a>cipher</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2773mcpsimp"><a name="p2773mcpsimp"></a><a name="p2773mcpsimp"></a>cipher 句柄</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2775mcpsimp"><a name="p2775mcpsimp"></a><a name="p2775mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2776mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2778mcpsimp"><a name="p2778mcpsimp"></a><a name="p2778mcpsimp"></a>keyslot</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2780mcpsimp"><a name="p2780mcpsimp"></a><a name="p2780mcpsimp"></a>keyslot句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2782mcpsimp"><a name="p2782mcpsimp"></a><a name="p2782mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2784mcpsimp"></a>
<table><thead align="left"><tr id="row2789mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2791mcpsimp"><a name="p2791mcpsimp"></a><a name="p2791mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2793mcpsimp"><a name="p2793mcpsimp"></a><a name="p2793mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2795mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2797mcpsimp"><a name="p2797mcpsimp"></a><a name="p2797mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2799mcpsimp"><a name="p2799mcpsimp"></a><a name="p2799mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2800mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2802mcpsimp"><a name="p2802mcpsimp"></a><a name="p2802mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2804mcpsimp"><a name="p2804mcpsimp"></a><a name="p2804mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   cipher、keyslot句柄必须已创建。在句柄未创建的情况下，句柄之间的绑定可能成功，但是会导致功能的失败。
-   绑定和解绑定必须成对使用。

【举例】

无。

## ss\_mpi\_cipher\_detach<a name="ZH-CN_TOPIC_0000002441653049"></a>

【描述】

对称加解密时cipher 句柄与keyslot句柄解绑定。

【语法】

```
td_s32 ss_mpi_cipher_detach(td_handle cipher, td_handle keyslot);
```

【参数】

<a name="table2822mcpsimp"></a>
<table><thead align="left"><tr id="row2828mcpsimp"><th class="cellrowborder" valign="top" width="27%" id="mcps1.1.4.1.1"><p id="p2830mcpsimp"><a name="p2830mcpsimp"></a><a name="p2830mcpsimp"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.4.1.2"><p id="p2832mcpsimp"><a name="p2832mcpsimp"></a><a name="p2832mcpsimp"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p2834mcpsimp"><a name="p2834mcpsimp"></a><a name="p2834mcpsimp"></a>输入/输出</p>
</th>
</tr>
</thead>
<tbody><tr id="row2836mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2838mcpsimp"><a name="p2838mcpsimp"></a><a name="p2838mcpsimp"></a>cipher</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2840mcpsimp"><a name="p2840mcpsimp"></a><a name="p2840mcpsimp"></a>cipher 句柄</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2842mcpsimp"><a name="p2842mcpsimp"></a><a name="p2842mcpsimp"></a>输入</p>
</td>
</tr>
<tr id="row2843mcpsimp"><td class="cellrowborder" valign="top" width="27%" headers="mcps1.1.4.1.1 "><p id="p2845mcpsimp"><a name="p2845mcpsimp"></a><a name="p2845mcpsimp"></a>keyslot</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.4.1.2 "><p id="p2847mcpsimp"><a name="p2847mcpsimp"></a><a name="p2847mcpsimp"></a>keyslot句柄。</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p2849mcpsimp"><a name="p2849mcpsimp"></a><a name="p2849mcpsimp"></a>输入</p>
</td>
</tr>
</tbody>
</table>

【返回值】

<a name="table2851mcpsimp"></a>
<table><thead align="left"><tr id="row2856mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p2858mcpsimp"><a name="p2858mcpsimp"></a><a name="p2858mcpsimp"></a>返回值</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p2860mcpsimp"><a name="p2860mcpsimp"></a><a name="p2860mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2862mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2864mcpsimp"><a name="p2864mcpsimp"></a><a name="p2864mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2866mcpsimp"><a name="p2866mcpsimp"></a><a name="p2866mcpsimp"></a>成功。</p>
</td>
</tr>
<tr id="row2867mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p2869mcpsimp"><a name="p2869mcpsimp"></a><a name="p2869mcpsimp"></a>非0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p2871mcpsimp"><a name="p2871mcpsimp"></a><a name="p2871mcpsimp"></a>参见<a href="错误码.md">错误码</a>。</p>
</td>
</tr>
</tbody>
</table>

【需求】

-   头文件：ot\_common\_cipher.h、ss\_mpi\_cipher.h
-   库文件：libss\_cipher.a、libss\_cipher.so

【注意】

-   cipher、keyslot句柄必须已创建。
-   绑定和解绑定必须成对使用。

【举例】

无。

# 数据类型
相关数据类型、数据结构定义如下（其他公共数据类型定义请参考ot\_type.h）：

-   [ot\_cipher\_work\_mode](#ZH-CN_TOPIC_0000002408093766)：定义CIPHER工作模式。
-   [ot\_cipher\_alg](#ZH-CN_TOPIC_0000002441572889)：定义CIPHER加密算法。
-   [ot\_cipher\_key\_len](#ZH-CN_TOPIC_0000002441653057)：定义CIPHER密钥长度。
-   [ot\_cipher\_bit\_width](#ZH-CN_TOPIC_0000002441572837)：定义CIPHER加密位宽。
-   [ot\_cipher\_ctrl\_chg\_flag](#ZH-CN_TOPIC_0000002408093706)：定义CIPHER 向量变更标志。
-   [ot\_cipher\_type](#ZH-CN_TOPIC_0000002441572897)：定义CIPHER加解密类型选择。
-   [ot\_cipher\_attr](#ZH-CN_TOPIC_0000002408093754)：定义CIPHER加解密属性结构体。
-   [ot\_cipher\_ctrl\_aes](#ZH-CN_TOPIC_0000002408253582)：AES加密控制信息结构体。
-   [ot\_cipher\_ctrl\_aes\_ccm\_gcm](#ZH-CN_TOPIC_0000002441572857)：AES-CCM、AES-GCM 加密控制信息结构体。
-   [ot\_cipher\_ctrl\_sm4](#ZH-CN_TOPIC_0000002408253642)：定义SM4加密控制信息结构体。
-   [ot\_cipher\_ctrl](#ZH-CN_TOPIC_0000002441652985)：定义加密控制信息结构体。
-   [ot\_cipher\_data](#ZH-CN_TOPIC_0000002441653005)：定义CIPHER加解密数据。
-   [ot\_cipher\_hash\_type](#ZH-CN_TOPIC_0000002441653037)：定义CIPHER哈希算法类型。
-   [ot\_cipher\_hash\_attr](#ZH-CN_TOPIC_0000002408253650)：定义CIPHER哈希算法初始化输入结构体。
-   [ot\_cipher\_common\_data](#ZH-CN_TOPIC_0000002408093682)：定义通用输入输出数据格式。
-   [ot\_cipher\_rsa\_scheme](#ZH-CN_TOPIC_0000002408253602)：定义RSA算法填充。
-   [ot\_cipher\_rsa\_public\_key](#ZH-CN_TOPIC_0000002408253666)：定义RSA公钥结构体。
-   [ot\_cipher\_rsa\_private\_key](#ZH-CN_TOPIC_0000002441653077)：定义RSA私钥结构体。
-   [ot\_cipher\_sign\_type](#ZH-CN_TOPIC_0000002441572853)：定义非对称算法签名验签输入数据类型。
-   [ot\_cipher\_sign\_in\_data](#ZH-CN_TOPIC_0000002408093714)：定义非对称算法签名验签输入数据结构体。
-   [ot\_cipher\_sm2\_public\_key](#ZH-CN_TOPIC_0000002408093742)：定义SM2公钥结构体。
-   [ot\_cipher\_sm2\_private\_key](#ZH-CN_TOPIC_0000002441572841)：定义SM2私钥结构体。
-   [ot\_cipher\_sm2\_sign](#ZH-CN_TOPIC_0000002441653013)：定义SM2签名结构体。
-   [ot\_cipher\_sm2\_verify](#ZH-CN_TOPIC_0000002441572885)：定义SM2验签结构体。
-   [ot\_cipher\_sm2\_sign\_data](#ZH-CN_TOPIC_0000002441653045)：定义SM2签名验签数据结构体。
-   [ot\_keyslot\_type](#ZH-CN_TOPIC_0000002441572929)：keyslot类型枚举值。
-   [ot\_keyslot\_secure\_mode](#ZH-CN_TOPIC_0000002441572873)：keyslot安全模式枚举值。
-   [ot\_keyslot\_attr](#ZH-CN_TOPIC_0000002408093730)：keyslot属性结构体。
-   [OT\_CIPHER\_MAX\_IV\_SIZE\_IN\_WORD](#ZH-CN_TOPIC_0000002441652981)：CIPHER 的IV最大长度。
-   [OT\_CIPHER\_SM2\_LEN\_IN\_WORD](#ZH-CN_TOPIC_0000002408093698)：SM2密钥、签名验签数据长度。































## ot\_cipher\_work\_mode<a name="ZH-CN_TOPIC_0000002408093766"></a>

【说明】

定义CIPHER工作模式。

【定义】

```
/* Cipher work mode */
typedef enum {
OT_CIPHER_WORK_MODE_ECB     = 0x0,
    OT_CIPHER_WORK_MODE_CBC,
    OT_CIPHER_WORK_MODE_CFB,
    OT_CIPHER_WORK_MODE_OFB,
    OT_CIPHER_WORK_MODE_CTR,
    OT_CIPHER_WORK_MODE_CCM,
    OT_CIPHER_WORK_MODE_GCM,
    OT_CIPHER_WORK_MODE_BUTT,
} ot_cipher_work_mode;
```

【成员】

<a name="table2980mcpsimp"></a>
<table><thead align="left"><tr id="row2985mcpsimp"><th class="cellrowborder" valign="top" width="45%" id="mcps1.1.3.1.1"><p id="p2987mcpsimp"><a name="p2987mcpsimp"></a><a name="p2987mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.3.1.2"><p id="p2989mcpsimp"><a name="p2989mcpsimp"></a><a name="p2989mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row2991mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p2993mcpsimp"><a name="p2993mcpsimp"></a><a name="p2993mcpsimp"></a>OT_CIPHER_WORK_MODE_ECB</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p2995mcpsimp"><a name="p2995mcpsimp"></a><a name="p2995mcpsimp"></a>ECB（Electronic CodeBook）模式。</p>
</td>
</tr>
<tr id="row2996mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p2998mcpsimp"><a name="p2998mcpsimp"></a><a name="p2998mcpsimp"></a>OT_CIPHER_WORK_MODE_CBC</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3000mcpsimp"><a name="p3000mcpsimp"></a><a name="p3000mcpsimp"></a>CBC（Cipher Block Chaining）模式。</p>
</td>
</tr>
<tr id="row3001mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p3003mcpsimp"><a name="p3003mcpsimp"></a><a name="p3003mcpsimp"></a>OT_CIPHER_WORK_MODE_CFB</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3005mcpsimp"><a name="p3005mcpsimp"></a><a name="p3005mcpsimp"></a>CFB（Cipher FeedBack）模式。</p>
</td>
</tr>
<tr id="row3006mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p3008mcpsimp"><a name="p3008mcpsimp"></a><a name="p3008mcpsimp"></a>OT_CIPHER_WORK_MODE_OFB</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3010mcpsimp"><a name="p3010mcpsimp"></a><a name="p3010mcpsimp"></a>OFB（Output FeedBack）模式。</p>
</td>
</tr>
<tr id="row3011mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p3013mcpsimp"><a name="p3013mcpsimp"></a><a name="p3013mcpsimp"></a>OT_CIPHER_WORK_MODE_CTR</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3015mcpsimp"><a name="p3015mcpsimp"></a><a name="p3015mcpsimp"></a>CTR（Counter）模式。</p>
</td>
</tr>
<tr id="row3016mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p3018mcpsimp"><a name="p3018mcpsimp"></a><a name="p3018mcpsimp"></a>OT_CIPHER_WORK_MODE_CCM</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3020mcpsimp"><a name="p3020mcpsimp"></a><a name="p3020mcpsimp"></a>CCM（Counter with Cipher Block Chaining-Message Authentication）模式。</p>
</td>
</tr>
<tr id="row3021mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p3023mcpsimp"><a name="p3023mcpsimp"></a><a name="p3023mcpsimp"></a>OT_CIPHER_WORK_MODE_GCM</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3025mcpsimp"><a name="p3025mcpsimp"></a><a name="p3025mcpsimp"></a>GCM（Galois/Counter Mode）模式。</p>
</td>
</tr>
<tr id="row3026mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p3028mcpsimp"><a name="p3028mcpsimp"></a><a name="p3028mcpsimp"></a>OT_CIPHER_WORK_MODE_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3030mcpsimp"><a name="p3030mcpsimp"></a><a name="p3030mcpsimp"></a>边界值，做边界检查使用，无效模式。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

ECB/CBC/CFB/OFB模式输入数据长度必须block对齐。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_alg<a name="ZH-CN_TOPIC_0000002441572889"></a>

【说明】

定义CIPHER加密算法。

【定义】

```
/* Cipher algorithm */
typedef enum {
    OT_CIPHER_ALG_AES           = 0x0,  /* Advanced encryption standard (AES) algorithm */
    OT_CIPHER_ALG_SM1,                  /* SM1 algorithm. */
    OT_CIPHER_ALG_SM4,                  /* SM4 algorithm. */
    OT_CIPHER_ALG_DMA,                  /* DMA copy. */
    OT_CIPHER_ALG_BUTT,
} ot_cipher_alg;
```

【成员】

<a name="table3054mcpsimp"></a>
<table><thead align="left"><tr id="row3059mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p3061mcpsimp"><a name="p3061mcpsimp"></a><a name="p3061mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p3063mcpsimp"><a name="p3063mcpsimp"></a><a name="p3063mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3065mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3067mcpsimp"><a name="p3067mcpsimp"></a><a name="p3067mcpsimp"></a>OT_CIPHER_ALG_AES</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3069mcpsimp"><a name="p3069mcpsimp"></a><a name="p3069mcpsimp"></a>AES算法。</p>
</td>
</tr>
<tr id="row3070mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3072mcpsimp"><a name="p3072mcpsimp"></a><a name="p3072mcpsimp"></a>OT_CIPHER_ALG_SM1</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3074mcpsimp"><a name="p3074mcpsimp"></a><a name="p3074mcpsimp"></a>SM1算法。</p>
</td>
</tr>
<tr id="row3075mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3077mcpsimp"><a name="p3077mcpsimp"></a><a name="p3077mcpsimp"></a>OT_CIPHER_ALG_SM4</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3079mcpsimp"><a name="p3079mcpsimp"></a><a name="p3079mcpsimp"></a>SM4算法。</p>
</td>
</tr>
<tr id="row3080mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3082mcpsimp"><a name="p3082mcpsimp"></a><a name="p3082mcpsimp"></a>OT_CIPHER_ALG_DMA</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3084mcpsimp"><a name="p3084mcpsimp"></a><a name="p3084mcpsimp"></a>DMA直接拷贝，不做加解密运算。</p>
</td>
</tr>
<tr id="row3085mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p3087mcpsimp"><a name="p3087mcpsimp"></a><a name="p3087mcpsimp"></a>OT_CIPHER_ALG_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3089mcpsimp"><a name="p3089mcpsimp"></a><a name="p3089mcpsimp"></a>边界值，做边界检查使用，无效算法。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

SS928V100、SS626V100不支持SM1、SM4。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_key\_len<a name="ZH-CN_TOPIC_0000002441653057"></a>

【说明】

定义CIPHER密钥长度。

【定义】

```
/* Key length */
typedef enum {
    OT_CIPHER_KEY_DEFAULT       = 0x0,
    OT_CIPHER_KEY_AES_128BIT     = 0x0,
    OT_CIPHER_KEY_AES_192BIT     = 0x1,
    OT_CIPHER_KEY_AES_256BIT     = 0x2,
    OT_CIPHER_KEY_LEN_BUTT      = 0x3,
} ot_cipher_key_len;
```

【成员】

<a name="table3113mcpsimp"></a>
<table><thead align="left"><tr id="row3118mcpsimp"><th class="cellrowborder" valign="top" width="46%" id="mcps1.1.3.1.1"><p id="p3120mcpsimp"><a name="p3120mcpsimp"></a><a name="p3120mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.1.3.1.2"><p id="p3122mcpsimp"><a name="p3122mcpsimp"></a><a name="p3122mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3124mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p id="p3126mcpsimp"><a name="p3126mcpsimp"></a><a name="p3126mcpsimp"></a>OT_CIPHER_KEY_DEFAULT</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p3128mcpsimp"><a name="p3128mcpsimp"></a><a name="p3128mcpsimp"></a>默认key长度，AES：16 byte，SM1：48 byte，SM4：16 byte</p>
</td>
</tr>
<tr id="row3129mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p id="p3131mcpsimp"><a name="p3131mcpsimp"></a><a name="p3131mcpsimp"></a>OT_CIPHER_KEY_AES_128BIT</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p3133mcpsimp"><a name="p3133mcpsimp"></a><a name="p3133mcpsimp"></a>AES运算方式下采用128bit密钥长度。</p>
</td>
</tr>
<tr id="row3134mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p id="p3136mcpsimp"><a name="p3136mcpsimp"></a><a name="p3136mcpsimp"></a>OT_CIPHER_KEY_AES_192BIT</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p3138mcpsimp"><a name="p3138mcpsimp"></a><a name="p3138mcpsimp"></a>AES运算方式下采用192bit密钥长度。</p>
</td>
</tr>
<tr id="row3139mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p id="p3141mcpsimp"><a name="p3141mcpsimp"></a><a name="p3141mcpsimp"></a>OT_CIPHER_KEY_AES_256BIT</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p3143mcpsimp"><a name="p3143mcpsimp"></a><a name="p3143mcpsimp"></a>AES运算方式下采用256bit密钥长度。</p>
</td>
</tr>
<tr id="row3144mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p id="p3146mcpsimp"><a name="p3146mcpsimp"></a><a name="p3146mcpsimp"></a>OT_CIPHER_KEY_LEN_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p3148mcpsimp"><a name="p3148mcpsimp"></a><a name="p3148mcpsimp"></a>边界值，做边界检查使用，无效Key长度。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

AES的密钥长度可以为128bit，192bit或256bit。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl\_aes](#ot_cipher_ctrl_aes)
-   [ot\_cipher\_ctrl\_aes\_ccm\_gcm](#ot_cipher_ctrl_aes_ccm_gcm)
-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_bit\_width<a name="ZH-CN_TOPIC_0000002441572837"></a>

【说明】

定义CIPHER加密位宽。

【定义】

```
/* Cipher bit width */
typedef enum {
    OT_CIPHER_BIT_WIDTH_1BIT    = 0x0,  /* 1-bit width */
    OT_CIPHER_BIT_WIDTH_8BIT    = 0x1,  /* 8-bit width */
    OT_CIPHER_BIT_WIDTH_64BIT   = 0x2,  /* 64-bit width */
    OT_CIPHER_BIT_WIDTH_128BIT  = 0x3,  /* 128-bit width */
    OT_CIPHER_BIT_WIDTH_BUTT,
} ot_cipher_bit_width;
```

【成员】

<a name="table3177mcpsimp"></a>
<table><thead align="left"><tr id="row3182mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p3184mcpsimp"><a name="p3184mcpsimp"></a><a name="p3184mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p3186mcpsimp"><a name="p3186mcpsimp"></a><a name="p3186mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3188mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3190mcpsimp"><a name="p3190mcpsimp"></a><a name="p3190mcpsimp"></a>OT_CIPHER_BIT_WIDTH_1BIT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3192mcpsimp"><a name="p3192mcpsimp"></a><a name="p3192mcpsimp"></a>1bit位宽。</p>
</td>
</tr>
<tr id="row3193mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3195mcpsimp"><a name="p3195mcpsimp"></a><a name="p3195mcpsimp"></a>OT_CIPHER_BIT_WIDTH_8BIT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3197mcpsimp"><a name="p3197mcpsimp"></a><a name="p3197mcpsimp"></a>8bit位宽。</p>
</td>
</tr>
<tr id="row3198mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3200mcpsimp"><a name="p3200mcpsimp"></a><a name="p3200mcpsimp"></a>OT_CIPHER_BIT_WIDTH_64BIT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3202mcpsimp"><a name="p3202mcpsimp"></a><a name="p3202mcpsimp"></a>64bit位宽。</p>
</td>
</tr>
<tr id="row3203mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3205mcpsimp"><a name="p3205mcpsimp"></a><a name="p3205mcpsimp"></a>OT_CIPHER_BIT_WIDTH_128BIT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3207mcpsimp"><a name="p3207mcpsimp"></a><a name="p3207mcpsimp"></a>128bit位宽。</p>
</td>
</tr>
<tr id="row3208mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3210mcpsimp"><a name="p3210mcpsimp"></a><a name="p3210mcpsimp"></a>OT_CIPHER_BIT_WIDTH_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3212mcpsimp"><a name="p3212mcpsimp"></a><a name="p3212mcpsimp"></a>边界值，做边界检查使用，无效位宽。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl\_aes](#ot_cipher_ctrl_aes)
-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_ctrl\_chg\_flag<a name="ZH-CN_TOPIC_0000002408093706"></a>

【说明】

定义CIPHER 向量变更标志。

【定义】

```
/* Cipher control parameters */
typedef enum {
    OT_CIPHER_IV_CHG_NONE = 0,            /** CIPHER set key and don't set IV */
    OT_CIPHER_IV_CHG_ONE_PACK,           /** CIPHER set key and IV for first package */
    OT_CIPHER_IV_CHG_ALL_PACK,            /** CIPHER set key and IV for all package */
    OT_CIPHER_IV_CHG_BUTT,
} ot_cipher_ctrl_chg_flag;
```

【成员】

<a name="table3238mcpsimp"></a>
<table><thead align="left"><tr id="row3243mcpsimp"><th class="cellrowborder" valign="top" width="45%" id="mcps1.1.3.1.1"><p id="p3245mcpsimp"><a name="p3245mcpsimp"></a><a name="p3245mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.3.1.2"><p id="p3247mcpsimp"><a name="p3247mcpsimp"></a><a name="p3247mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3249mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3251mcpsimp"><a name="p3251mcpsimp"></a><a name="p3251mcpsimp"></a>OT_CIPHER_IV_CHG_NONE</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3253mcpsimp"><a name="p3253mcpsimp"></a><a name="p3253mcpsimp"></a>更新密钥，不更新向量</p>
</td>
</tr>
<tr id="row3254mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3256mcpsimp"><a name="p3256mcpsimp"></a><a name="p3256mcpsimp"></a>OT_CIPHER_IV_CHG_ONE_PACK</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3258mcpsimp"><a name="p3258mcpsimp"></a><a name="p3258mcpsimp"></a>为第一个数据包更新向量和密钥</p>
</td>
</tr>
<tr id="row3259mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p19436145744912"><a name="p19436145744912"></a><a name="p19436145744912"></a>OT_CIPHER_IV_CHG_ALL_PACK</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3263mcpsimp"><a name="p3263mcpsimp"></a><a name="p3263mcpsimp"></a>为所有数据包更新向量和密钥</p>
</td>
</tr>
<tr id="row3264mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3266mcpsimp"><a name="p3266mcpsimp"></a><a name="p3266mcpsimp"></a>OT_CIPHER_IV_CHG_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3268mcpsimp"><a name="p3268mcpsimp"></a><a name="p3268mcpsimp"></a>边界值，做边界检查使用，无效。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl\_aes](#ot_cipher_ctrl_aes)
-   [ot\_cipher\_ctrl\_sm4](#ot_cipher_ctrl_sm4)
-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_type<a name="ZH-CN_TOPIC_0000002441572897"></a>

【说明】

定义CIPHER加解密类型选择。

【定义】

```
/* Encryption/Decryption type selecting */
typedef enum {
    OT_CIPHER_TYPE_NORMAL       = 0x0,
    OT_CIPHER_TYPE_BUTT,
} ot_cipher_type;
```

【成员】

<a name="table3294mcpsimp"></a>
<table><thead align="left"><tr id="row3299mcpsimp"><th class="cellrowborder" valign="top" width="45%" id="mcps1.1.3.1.1"><p id="p3301mcpsimp"><a name="p3301mcpsimp"></a><a name="p3301mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.3.1.2"><p id="p3303mcpsimp"><a name="p3303mcpsimp"></a><a name="p3303mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3305mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3307mcpsimp"><a name="p3307mcpsimp"></a><a name="p3307mcpsimp"></a>OT_CIPHER_TYPE_NORMAL</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3309mcpsimp"><a name="p3309mcpsimp"></a><a name="p3309mcpsimp"></a>1-15通道DMA方式。</p>
</td>
</tr>
<tr id="row3310mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3312mcpsimp"><a name="p3312mcpsimp"></a><a name="p3312mcpsimp"></a>OT_CIPHER_TYPE_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p3314mcpsimp"><a name="p3314mcpsimp"></a><a name="p3314mcpsimp"></a>边界值，做边界检查使用，无效通道类型。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [ot\_cipher\_attr](#ot_cipher_attr)
-   [ss\_mpi\_cipher\_create](#ss_mpi_cipher_create)

## ot\_cipher\_attr<a name="ZH-CN_TOPIC_0000002408093754"></a>

【说明】

定义CIPHER加解密属性结构体。

【定义】

```
/* Structure of the cipher type */
typedef struct {
    ot_cipher_type cipher_type;
} ot_cipher_attr;
```

【成员】

<a name="table3334mcpsimp"></a>
<table><thead align="left"><tr id="row3339mcpsimp"><th class="cellrowborder" valign="top" width="59%" id="mcps1.1.3.1.1"><p id="p3341mcpsimp"><a name="p3341mcpsimp"></a><a name="p3341mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.1.3.1.2"><p id="p3343mcpsimp"><a name="p3343mcpsimp"></a><a name="p3343mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3345mcpsimp"><td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3347mcpsimp"><a name="p3347mcpsimp"></a><a name="p3347mcpsimp"></a>cipher_type</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.2 "><p id="p3349mcpsimp"><a name="p3349mcpsimp"></a><a name="p3349mcpsimp"></a>加密类型结构体变量。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

[ss\_mpi\_cipher\_create](#ss_mpi_cipher_create)

## ot\_cipher\_ctrl\_aes<a name="ZH-CN_TOPIC_0000002408253582"></a>

【说明】

AES加密控制信息结构体。

【定义】

```
/* Structure of the cipher AES control information */
typedef struct {
    td_u32 iv[OT_CIPHER_MAX_IV_SIZE_IN_WORD];   /* Initialization vector (IV) for 4 byte */
    ot_cipher_bit_width bit_width;                  /* Bit width for encryption or decryption */
    ot_cipher_key_len key_len;                     /* Key length */
    ot_cipher_ctrl_chg_flag chg_flags;
} ot_cipher_ctrl_aes;
```

【成员】

<a name="table3372mcpsimp"></a>
<table><thead align="left"><tr id="row3377mcpsimp"><th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.1"><p id="p3379mcpsimp"><a name="p3379mcpsimp"></a><a name="p3379mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.2"><p id="p3381mcpsimp"><a name="p3381mcpsimp"></a><a name="p3381mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3383mcpsimp"><td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.1 "><p id="p3385mcpsimp"><a name="p3385mcpsimp"></a><a name="p3385mcpsimp"></a>iv[<a href="OT_CIPHER_MAX_IV_SIZE_IN_WORD.md">OT_CIPHER_MAX_IV_SIZE_IN_WORD</a>]</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.2 "><p id="p3388mcpsimp"><a name="p3388mcpsimp"></a><a name="p3388mcpsimp"></a>向量</p>
</td>
</tr>
<tr id="row3389mcpsimp"><td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.1 "><p id="p3391mcpsimp"><a name="p3391mcpsimp"></a><a name="p3391mcpsimp"></a>bit_width</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.2 "><p id="p3393mcpsimp"><a name="p3393mcpsimp"></a><a name="p3393mcpsimp"></a>加密位宽</p>
</td>
</tr>
<tr id="row3394mcpsimp"><td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.1 "><p id="p3396mcpsimp"><a name="p3396mcpsimp"></a><a name="p3396mcpsimp"></a>key_len</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.2 "><p id="p3398mcpsimp"><a name="p3398mcpsimp"></a><a name="p3398mcpsimp"></a>加密Key长度</p>
</td>
</tr>
<tr id="row3399mcpsimp"><td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.1 "><p id="p3401mcpsimp"><a name="p3401mcpsimp"></a><a name="p3401mcpsimp"></a>chg_flags</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.2 "><p id="p3403mcpsimp"><a name="p3403mcpsimp"></a><a name="p3403mcpsimp"></a>向量变更标志</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

AES支持的工作模式为：ECB/CBC/CFB/OFB/CTR，其中CFB支持的位宽可以为1、8、128bit，OFB模式仅支持128bit位宽。其他模式默认只支持128bit位宽。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_ctrl\_aes\_ccm\_gcm<a name="ZH-CN_TOPIC_0000002441572857"></a>

【说明】

AES-CCM、AES-GCM加密控制信息结构体。

【定义】

```
/* Structure of the cipher AES CCM/GCM control information */
typedef struct {
    td_u32 iv[OT_CIPHER_MAX_IV_SIZE_IN_WORD];
    ot_cipher_key_len key_len;
    td_u32 iv_len;
    td_u32 tag_len;
    td_u32 aad_len;
    td_phys_addr_t aad_phys_addr;
    td_u8 *aad_addr;
} ot_cipher_ctrl_aes_ccm_gcm;
```

【成员】

<a name="table3435mcpsimp"></a>
<table><thead align="left"><tr id="row3440mcpsimp"><th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.3.1.1"><p id="p3442mcpsimp"><a name="p3442mcpsimp"></a><a name="p3442mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.3.1.2"><p id="p3444mcpsimp"><a name="p3444mcpsimp"></a><a name="p3444mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3446mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p3448mcpsimp"><a name="p3448mcpsimp"></a><a name="p3448mcpsimp"></a>iv[<a href="OT_CIPHER_MAX_IV_SIZE_IN_WORD.md">OT_CIPHER_MAX_IV_SIZE_IN_WORD</a>]</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p3451mcpsimp"><a name="p3451mcpsimp"></a><a name="p3451mcpsimp"></a>向量IV</p>
</td>
</tr>
<tr id="row3452mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p3454mcpsimp"><a name="p3454mcpsimp"></a><a name="p3454mcpsimp"></a>key_len</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p3456mcpsimp"><a name="p3456mcpsimp"></a><a name="p3456mcpsimp"></a>加密Key长度</p>
</td>
</tr>
<tr id="row3457mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p3459mcpsimp"><a name="p3459mcpsimp"></a><a name="p3459mcpsimp"></a>iv_len</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p3461mcpsimp"><a name="p3461mcpsimp"></a><a name="p3461mcpsimp"></a>向量IV长度</p>
</td>
</tr>
<tr id="row3462mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p3464mcpsimp"><a name="p3464mcpsimp"></a><a name="p3464mcpsimp"></a>tag_len</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p3466mcpsimp"><a name="p3466mcpsimp"></a><a name="p3466mcpsimp"></a>TAG长度</p>
</td>
</tr>
<tr id="row3467mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p3469mcpsimp"><a name="p3469mcpsimp"></a><a name="p3469mcpsimp"></a>aad_len</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p3471mcpsimp"><a name="p3471mcpsimp"></a><a name="p3471mcpsimp"></a>关联数据A的长度</p>
</td>
</tr>
<tr id="row3472mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p18792164418120"><a name="p18792164418120"></a><a name="p18792164418120"></a>aad_phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p3476mcpsimp"><a name="p3476mcpsimp"></a><a name="p3476mcpsimp"></a>关联数据A的物理地址</p>
</td>
</tr>
<tr id="row617004814294"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p1417064872911"><a name="p1417064872911"></a><a name="p1417064872911"></a>aad_addr</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p8170114813297"><a name="p8170114813297"></a><a name="p8170114813297"></a>保留参数，后续用于关联数据A的地址类型拓展。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

-   对于CCM：向量iv长度iv\_len可取\{7, 8, 9, 10, 11, 12, 13\} byte，iv存放算法标准中的Nonce数据N。加密数据的长度用n个Byte表示，且应满足条件：iv\_len+n=15。因此，iv\_len为13时，n为2，此时加密数据长度最长为65535byte，其它以此类推。tag的长度tag\_len可取\{4, 6, 8, 10, 12, 14, 16\}byte，CCM加密时的向量N、关联数据A取值必须与解密时保持一致。
-   对于GCM：向量iv长度iv\_len可取范围为\[1\~16\]byte，tag的长度tag\_len可为\{12, 13, 14, 15, 16\}byte，特殊情况可取4、8byte，GCM加密时的关联数据A取值必须与解密时保持一致。
-   linux平台关联数据A只支持物理地址，optee平台关联数据A只支持虚拟地址，linux平台请将物理地址传给aad\_phys\_addr，optee平台请将虚拟地址传给aad\_phys\_addr。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_ctrl\_sm4<a name="ZH-CN_TOPIC_0000002408253642"></a>

【说明】

定义SM4加密控制信息结构体。

【定义】

```
/* Structure of the cipher SM4 control information */
typedef struct {
    td_u32 iv[OT_CIPHER_MAX_IV_SIZE_IN_WORD];    /* (IV) */
    ot_cipher_ctrl_chg_flag chg_flags;
} ot_cipher_ctrl_sm4;
```

【成员】

<a name="table3505mcpsimp"></a>
<table><thead align="left"><tr id="row3510mcpsimp"><th class="cellrowborder" valign="top" width="54%" id="mcps1.1.3.1.1"><p id="p3512mcpsimp"><a name="p3512mcpsimp"></a><a name="p3512mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="46%" id="mcps1.1.3.1.2"><p id="p3514mcpsimp"><a name="p3514mcpsimp"></a><a name="p3514mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3516mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.1 "><p id="p3518mcpsimp"><a name="p3518mcpsimp"></a><a name="p3518mcpsimp"></a><span xml:lang="de-DE" id="ph3519mcpsimp"><a name="ph3519mcpsimp"></a><a name="ph3519mcpsimp"></a>iv[</span><a href="OT_CIPHER_MAX_IV_SIZE_IN_WORD.md">OT_CIPHER_MAX_IV_SIZE_IN_WORD</a><span xml:lang="de-DE" id="ph3521mcpsimp"><a name="ph3521mcpsimp"></a><a name="ph3521mcpsimp"></a>]</span></p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.2 "><p id="p3523mcpsimp"><a name="p3523mcpsimp"></a><a name="p3523mcpsimp"></a>向量</p>
</td>
</tr>
<tr id="row3524mcpsimp"><td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3526mcpsimp"><a name="p3526mcpsimp"></a><a name="p3526mcpsimp"></a>chg_flags</p>
</td>
<td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.2 "><p id="p3528mcpsimp"><a name="p3528mcpsimp"></a><a name="p3528mcpsimp"></a>向量变更标志</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

-   SM4支持的工作模式为：ECB/CBC/CFB/OFB/CTR，其中CFB支持的位宽可以为1、8、128bit，OFB模式仅支持128bit位宽。
-   ECB模式可以不配置iv。
-   SS928V100、SS626V100不支持SM4。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_ctrl<a name="ZH-CN_TOPIC_0000002441652985"></a>

【说明】

定义加密控制信息结构体。

【定义】

```
/* Structure of the cipher control information */
typedef struct {
    ot_cipher_alg alg;                                     /* cipher algorithm */
    ot_cipher_work_mode work_mode;                      /* algorithm work mode */
    union {
        ot_cipher_ctrl_aes aes_ctrl;                         /* AES ECB/CBC/CFB/OFB/CTR control */
        ot_cipher_ctrl_aes_ccm_gcm aes_ccm_gcm_ctrl;       /* AES CCM/GCM control */
        ot_cipher_ctrl_sm4 sm4_ctrl;                        /* SM4 ECB/CBC/CFB/OFB/CTR control */
    };
} ot_cipher_ctrl;
```

【成员】

<a name="table3567mcpsimp"></a>
<table><thead align="left"><tr id="row3572mcpsimp"><th class="cellrowborder" valign="top" width="46%" id="mcps1.1.3.1.1"><p id="p3574mcpsimp"><a name="p3574mcpsimp"></a><a name="p3574mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.1.3.1.2"><p id="p3576mcpsimp"><a name="p3576mcpsimp"></a><a name="p3576mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3578mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3580mcpsimp"><a name="p3580mcpsimp"></a><a name="p3580mcpsimp"></a>alg</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p3582mcpsimp"><a name="p3582mcpsimp"></a><a name="p3582mcpsimp"></a>对称加解密算法</p>
</td>
</tr>
<tr id="row3583mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3585mcpsimp"><a name="p3585mcpsimp"></a><a name="p3585mcpsimp"></a>work_mode</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p3587mcpsimp"><a name="p3587mcpsimp"></a><a name="p3587mcpsimp"></a>对称算法工作模式</p>
</td>
</tr>
<tr id="row3588mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3590mcpsimp"><a name="p3590mcpsimp"></a><a name="p3590mcpsimp"></a>aes_ctrl</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p3592mcpsimp"><a name="p3592mcpsimp"></a><a name="p3592mcpsimp"></a>AES ECB/CBC/CFB/OFB/CTR控制信息</p>
</td>
</tr>
<tr id="row3593mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3595mcpsimp"><a name="p3595mcpsimp"></a><a name="p3595mcpsimp"></a>aes_ccm_gcm_ctrl</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p3597mcpsimp"><a name="p3597mcpsimp"></a><a name="p3597mcpsimp"></a>AES CCM/GCM 控制信息</p>
</td>
</tr>
<tr id="row3598mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3600mcpsimp"><a name="p3600mcpsimp"></a><a name="p3600mcpsimp"></a>sm4_ctrl</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p3602mcpsimp"><a name="p3602mcpsimp"></a><a name="p3602mcpsimp"></a>SM4 ECB/CBC/CFB/OFB/CTR控制信息</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

-   当算法 alg 为 OT\_CIPHER\_ALG\_AES 且工作模式 work\_mode 为 OT\_CIPHER\_WORK\_MODE\_ECB、OT\_CIPHER\_WORK\_MODE\_CBC、OT\_CIPHER\_WORK\_MODE\_CFB、OT\_CIPHER\_WORK\_MODE\_OFB、OT\_CIPHER\_WORK\_MODE\_CTR中的一种时，联合体指向的结构体为  [ot\_cipher\_ctrl\_aes](#ZH-CN_TOPIC_0000002408253582)。
-   当算法 alg 为 OT\_CIPHER\_ALG\_AES 且工作模式 work\_mode 为 OT\_CIPHER\_WORK\_MODE\_CCM、OT\_CIPHER\_WORK\_MODE\_GCM中的一种时，联合体指向的结构体为  [ot\_cipher\_ctrl\_aes\_ccm\_gcm](#ZH-CN_TOPIC_0000002441572857)。
-   当算法 alg 为 OT\_CIPHER\_ALG\_SM4 且工作模式 work\_mode 为 OT\_CIPHER\_WORK\_MODE\_ECB、OT\_CIPHER\_WORK\_MODE\_CBC、OT\_CIPHER\_WORK\_MODE\_CFB、OT\_CIPHER\_WORK\_MODE\_OFB、OT\_CIPHER\_WORK\_MODE\_CTR中的一种时，联合体指向的结构体为  [ot\_cipher\_ctrl\_sm4](#ZH-CN_TOPIC_0000002408253642)。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## ot\_cipher\_data<a name="ZH-CN_TOPIC_0000002441653005"></a>

【说明】

定义CIPHER加解密数据。

【定义】

```
/* Cipher data */
typedef struct {
    td_phys_addr_t src_phys_addr;       /* phy address of the original data */
    td_phys_addr_t dst_phys_addr;       /* phy address of the purpose data */
    td_u32 byte_len;                    /* cipher data length*/
} ot_cipher_data;
```

【成员】

<a name="table3633mcpsimp"></a>
<table><thead align="left"><tr id="row3638mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p3640mcpsimp"><a name="p3640mcpsimp"></a><a name="p3640mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p3642mcpsimp"><a name="p3642mcpsimp"></a><a name="p3642mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3644mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3646mcpsimp"><a name="p3646mcpsimp"></a><a name="p3646mcpsimp"></a>src_phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3648mcpsimp"><a name="p3648mcpsimp"></a><a name="p3648mcpsimp"></a>源数据物理地址。</p>
</td>
</tr>
<tr id="row3649mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3651mcpsimp"><a name="p3651mcpsimp"></a><a name="p3651mcpsimp"></a>dst_phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3653mcpsimp"><a name="p3653mcpsimp"></a><a name="p3653mcpsimp"></a>目的数据物理地址。</p>
</td>
</tr>
<tr id="row3654mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3656mcpsimp"><a name="p3656mcpsimp"></a><a name="p3656mcpsimp"></a>byte_len</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3658mcpsimp"><a name="p3658mcpsimp"></a><a name="p3658mcpsimp"></a>加解密数据长度。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_encrypt\_multi\_pack](#ss_mpi_cipher_encrypt_multi_pack)
-   [ss\_mpi\_cipher\_decrypt\_multi\_pack](#ss_mpi_cipher_decrypt_multi_pack)

## ot\_cipher\_hash\_type<a name="ZH-CN_TOPIC_0000002441653037"></a>

【说明】

定义CIPHER哈希算法类型。

【定义】

```
/* Hash algorithm type */
typedef enum {
    OT_CIPHER_HASH_TYPE_SHA1         = 0x00,
    OT_CIPHER_HASH_TYPE_SHA224,
    OT_CIPHER_HASH_TYPE_SHA256,
    OT_CIPHER_HASH_TYPE_SHA384,
    OT_CIPHER_HASH_TYPE_SHA512,
    OT_CIPHER_HASH_TYPE_SM3          =  0x10,
    OT_CIPHER_HASH_TYPE_HMAC_SHA1    =  0x20,
    OT_CIPHER_HASH_TYPE_HMAC_SHA224,
    OT_CIPHER_HASH_TYPE_HMAC_SHA256,
    OT_CIPHER_HASH_TYPE_HMAC_SHA384,
    OT_CIPHER_HASH_TYPE_HMAC_SHA512,
    OT_CIPHER_HASH_TYPE_HMAC_SM3     =  0x30,
    OT_CIPHER_HASH_TYPE_BUTT,
} ot_cipher_hash_type;
```

【成员】

<a name="table3689mcpsimp"></a>
<table><thead align="left"><tr id="row3694mcpsimp"><th class="cellrowborder" valign="top" width="52%" id="mcps1.1.3.1.1"><p id="p3696mcpsimp"><a name="p3696mcpsimp"></a><a name="p3696mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.1.3.1.2"><p id="p3698mcpsimp"><a name="p3698mcpsimp"></a><a name="p3698mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3700mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3702mcpsimp"><a name="p3702mcpsimp"></a><a name="p3702mcpsimp"></a>OT_CIPHER_HASH_TYPE_SHA1</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3704mcpsimp"><a name="p3704mcpsimp"></a><a name="p3704mcpsimp"></a>SHA1哈希算法。</p>
</td>
</tr>
<tr id="row3705mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3707mcpsimp"><a name="p3707mcpsimp"></a><a name="p3707mcpsimp"></a>OT_CIPHER_HASH_TYPE_SHA224</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3709mcpsimp"><a name="p3709mcpsimp"></a><a name="p3709mcpsimp"></a>SHA224哈希算法。</p>
</td>
</tr>
<tr id="row3710mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3712mcpsimp"><a name="p3712mcpsimp"></a><a name="p3712mcpsimp"></a>OT_CIPHER_HASH_TYPE_SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3714mcpsimp"><a name="p3714mcpsimp"></a><a name="p3714mcpsimp"></a>SHA256哈希算法。</p>
</td>
</tr>
<tr id="row3715mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3717mcpsimp"><a name="p3717mcpsimp"></a><a name="p3717mcpsimp"></a>OT_CIPHER_HASH_TYPE_SHA384</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3719mcpsimp"><a name="p3719mcpsimp"></a><a name="p3719mcpsimp"></a>SHA384哈希算法。</p>
</td>
</tr>
<tr id="row3720mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3722mcpsimp"><a name="p3722mcpsimp"></a><a name="p3722mcpsimp"></a>OT_CIPHER_HASH_TYPE_SHA512</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3724mcpsimp"><a name="p3724mcpsimp"></a><a name="p3724mcpsimp"></a>SHA512哈希算法。</p>
</td>
</tr>
<tr id="row3725mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3727mcpsimp"><a name="p3727mcpsimp"></a><a name="p3727mcpsimp"></a>OT_CIPHER_HASH_TYPE_SM3</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3729mcpsimp"><a name="p3729mcpsimp"></a><a name="p3729mcpsimp"></a>SM3 杂凑算法</p>
</td>
</tr>
<tr id="row3730mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3732mcpsimp"><a name="p3732mcpsimp"></a><a name="p3732mcpsimp"></a>OT_CIPHER_HASH_TYPE_HMAC_SHA1</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3734mcpsimp"><a name="p3734mcpsimp"></a><a name="p3734mcpsimp"></a>HMAC_SHA1哈希算法。</p>
</td>
</tr>
<tr id="row3735mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3737mcpsimp"><a name="p3737mcpsimp"></a><a name="p3737mcpsimp"></a>OT_CIPHER_HASH_TYPE_HMAC_SHA224</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3739mcpsimp"><a name="p3739mcpsimp"></a><a name="p3739mcpsimp"></a>HMAC_SHA224哈希算法。</p>
</td>
</tr>
<tr id="row3740mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3742mcpsimp"><a name="p3742mcpsimp"></a><a name="p3742mcpsimp"></a>OT_CIPHER_HASH_TYPE_HMAC_SHA256</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3744mcpsimp"><a name="p3744mcpsimp"></a><a name="p3744mcpsimp"></a>HMAC_SHA256哈希算法。</p>
</td>
</tr>
<tr id="row3745mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3747mcpsimp"><a name="p3747mcpsimp"></a><a name="p3747mcpsimp"></a>OT_CIPHER_HASH_TYPE_HMAC_SHA384</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3749mcpsimp"><a name="p3749mcpsimp"></a><a name="p3749mcpsimp"></a>HMAC_SHA384哈希算法。</p>
</td>
</tr>
<tr id="row3750mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3752mcpsimp"><a name="p3752mcpsimp"></a><a name="p3752mcpsimp"></a>OT_CIPHER_HASH_TYPE_HMAC_SHA512</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3754mcpsimp"><a name="p3754mcpsimp"></a><a name="p3754mcpsimp"></a>HMAC_SHA512哈希算法。</p>
</td>
</tr>
<tr id="row3755mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3757mcpsimp"><a name="p3757mcpsimp"></a><a name="p3757mcpsimp"></a>OT_CIPHER_HASH_TYPE_HMAC_SM3</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3759mcpsimp"><a name="p3759mcpsimp"></a><a name="p3759mcpsimp"></a>HMAC_SM3杂凑算法。</p>
</td>
</tr>
<tr id="row3760mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3762mcpsimp"><a name="p3762mcpsimp"></a><a name="p3762mcpsimp"></a>OT_CIPHER_HASH_TYPE_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p3764mcpsimp"><a name="p3764mcpsimp"></a><a name="p3764mcpsimp"></a>边界值，做边界检查使用，无效算法。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

-   不支持SHA1、SHA224、HMAC-SHA1、HMAC-SHA224。
-   SS928V100、SS626V100不支持SM3、HMAC-SM3。

【相关数据类型及接口】

-   [ot\_cipher\_hash\_attr](#ot_cipher_hash_attr)
-   [ss\_mpi\_cipher\_hash\_init](#ss_mpi_cipher_hash_init)

## ot\_cipher\_hash\_attr<a name="ZH-CN_TOPIC_0000002408253650"></a>

【说明】

定义CIPHER哈希算法初始化输入结构体。

【定义】

```
/* Hash init struct input */
typedef struct {
    td_u8 *hmac_key;
    td_u32 hmac_key_len;
    ot_cipher_hash_type sha_type;
} ot_cipher_hash_attr;
```

【成员】

<a name="table3788mcpsimp"></a>
<table><thead align="left"><tr id="row3793mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p3795mcpsimp"><a name="p3795mcpsimp"></a><a name="p3795mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p3797mcpsimp"><a name="p3797mcpsimp"></a><a name="p3797mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3799mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3801mcpsimp"><a name="p3801mcpsimp"></a><a name="p3801mcpsimp"></a>hmac_key</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3803mcpsimp"><a name="p3803mcpsimp"></a><a name="p3803mcpsimp"></a>HMAC 密钥。</p>
</td>
</tr>
<tr id="row3804mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3806mcpsimp"><a name="p3806mcpsimp"></a><a name="p3806mcpsimp"></a>hmac_key_len</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3808mcpsimp"><a name="p3808mcpsimp"></a><a name="p3808mcpsimp"></a>HMAC 密钥长度。</p>
</td>
</tr>
<tr id="row3809mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3811mcpsimp"><a name="p3811mcpsimp"></a><a name="p3811mcpsimp"></a>sha_type</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3813mcpsimp"><a name="p3813mcpsimp"></a><a name="p3813mcpsimp"></a>选择哈希算法类型。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

[ss\_mpi\_cipher\_hash\_init](#ss_mpi_cipher_hash_init)

## ot\_cipher\_common\_data<a name="ZH-CN_TOPIC_0000002408093682"></a>

【说明】

定义通用输入输出数据格式结构体。

【定义】

```
typedef struct {
    td_u8 *data;
    td_u32 data_len;
} ot_cipher_common_data;
```

【成员】

<a name="table3829mcpsimp"></a>
<table><thead align="left"><tr id="row3834mcpsimp"><th class="cellrowborder" valign="top" width="39%" id="mcps1.1.3.1.1"><p id="p3836mcpsimp"><a name="p3836mcpsimp"></a><a name="p3836mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.3.1.2"><p id="p3838mcpsimp"><a name="p3838mcpsimp"></a><a name="p3838mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3840mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3842mcpsimp"><a name="p3842mcpsimp"></a><a name="p3842mcpsimp"></a>data</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p3844mcpsimp"><a name="p3844mcpsimp"></a><a name="p3844mcpsimp"></a>输入输出的数据。</p>
</td>
</tr>
<tr id="row3845mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3847mcpsimp"><a name="p3847mcpsimp"></a><a name="p3847mcpsimp"></a>data_len</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p3849mcpsimp"><a name="p3849mcpsimp"></a><a name="p3849mcpsimp"></a>输入输出的数据长度（单位：byte）。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

data\_len作为输入时，为输入的缓冲区长度；作为输出时，即是输出的缓冲区长度，同时也是输出数据的长度，缓冲区长度不能小于输出数据的长度。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_rsa\_public\_encrypt](#ss_mpi_cipher_rsa_public_encrypt)
-   [ss\_mpi\_cipher\_rsa\_private\_decrypt](#ss_mpi_cipher_rsa_private_decrypt)
-   [ss\_mpi\_cipher\_rsa\_private\_encrypt](#ss_mpi_cipher_rsa_private_encrypt)
-   [ss\_mpi\_cipher\_rsa\_public\_decrypt](#ss_mpi_cipher_rsa_public_decrypt)
-   [ss\_mpi\_cipher\_rsa\_sign](#ss_mpi_cipher_rsa_sign)
-   [ss\_mpi\_cipher\_rsa\_verify](#ss_mpi_cipher_rsa_verify)
-   [ss\_mpi\_cipher\_sm2\_encrypt](#ss_mpi_cipher_sm2_encrypt)
-   [ss\_mpi\_cipher\_sm2\_decrypt](#ss_mpi_cipher_sm2_decrypt)

## ot\_cipher\_rsa\_scheme<a name="ZH-CN_TOPIC_0000002408253602"></a>

【说明】

定义RSA算法填充方式。

【定义】

```
typedef enum {
    OT_CIPHER_RSA_SCHEME_PKCS1_V15 = 0x00,  /* PKCS#1 V15 */
    OT_CIPHER_RSA_SCHEME_PKCS1_V21,         /* PKCS#1 V21, PSS for signing, OAEP for encryption */
    OT_CIPHER_RSA_SCHEME_BUTT,
} ot_cipher_rsa_scheme;
```

【成员】

<a name="table3881mcpsimp"></a>
<table><thead align="left"><tr id="row3886mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p3888mcpsimp"><a name="p3888mcpsimp"></a><a name="p3888mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p3890mcpsimp"><a name="p3890mcpsimp"></a><a name="p3890mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3892mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3894mcpsimp"><a name="p3894mcpsimp"></a><a name="p3894mcpsimp"></a>OT_CIPHER_RSA_SCHEME_PKCS1_V15</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p3896mcpsimp"><a name="p3896mcpsimp"></a><a name="p3896mcpsimp"></a><span xml:lang="en-US" id="ph3897mcpsimp"><a name="ph3897mcpsimp"></a><a name="ph3897mcpsimp"></a>填充算法</span> PKCS#1 V15<span xml:lang="en-US" id="ph3898mcpsimp"><a name="ph3898mcpsimp"></a><a name="ph3898mcpsimp"></a>。</span></p>
</td>
</tr>
<tr id="row3899mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3901mcpsimp"><a name="p3901mcpsimp"></a><a name="p3901mcpsimp"></a>OT_CIPHER_RSA_SCHEME_PKCS1_V21</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p3903mcpsimp"><a name="p3903mcpsimp"></a><a name="p3903mcpsimp"></a>填充算法 PKCS#1 V21，对于签名是 PSS算法，对于加解密时 OAEP 算法。</p>
</td>
</tr>
<tr id="row3904mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3906mcpsimp"><a name="p3906mcpsimp"></a><a name="p3906mcpsimp"></a>OT_CIPHER_RSA_SCHEME_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p3908mcpsimp"><a name="p3908mcpsimp"></a><a name="p3908mcpsimp"></a>边界值，做边界检查使用，无效填充方式。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

建议使用PKCS\#1 V21填充方式，其他方式为弱填充或不安全填充方式。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_rsa\_public\_encrypt](#ss_mpi_cipher_rsa_public_encrypt)
-   [ss\_mpi\_cipher\_rsa\_private\_decrypt](#ss_mpi_cipher_rsa_private_decrypt)
-   [ss\_mpi\_cipher\_rsa\_private\_encrypt](#ss_mpi_cipher_rsa_private_encrypt)
-   [ss\_mpi\_cipher\_rsa\_public\_decrypt](#ss_mpi_cipher_rsa_public_decrypt)
-   [ss\_mpi\_cipher\_rsa\_sign](#ss_mpi_cipher_rsa_sign)
-   [ss\_mpi\_cipher\_rsa\_verify](#ss_mpi_cipher_rsa_verify)

## ot\_cipher\_rsa\_public\_key<a name="ZH-CN_TOPIC_0000002408253666"></a>

【说明】

定义RSA公钥结构体。

【定义】

```
/* RSA pub key struct */
typedef struct {
    td_u8  *n;      /* Point to pub modulus  */
    td_u8  *e;      /* Point to pub exponent */
    td_u16 n_len;   /* Length of pub modulus, max value is 512Byte */
    td_u16 e_len;   /* Length of pub exponent, max value is 512Byte */
} ot_cipher_rsa_public_key;
```

【成员】

<a name="table3938mcpsimp"></a>
<table><thead align="left"><tr id="row3943mcpsimp"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.3.1.1"><p id="p3945mcpsimp"><a name="p3945mcpsimp"></a><a name="p3945mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="70%" id="mcps1.1.3.1.2"><p id="p3947mcpsimp"><a name="p3947mcpsimp"></a><a name="p3947mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row3949mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3951mcpsimp"><a name="p3951mcpsimp"></a><a name="p3951mcpsimp"></a>n</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p id="p3953mcpsimp"><a name="p3953mcpsimp"></a><a name="p3953mcpsimp"></a>指向RSA公钥N的指针</p>
</td>
</tr>
<tr id="row3954mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3956mcpsimp"><a name="p3956mcpsimp"></a><a name="p3956mcpsimp"></a>e</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p3958mcpsimp"><a name="p3958mcpsimp"></a><a name="p3958mcpsimp"></a>指向RSA公钥E的指针</p>
</td>
</tr>
<tr id="row3959mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3961mcpsimp"><a name="p3961mcpsimp"></a><a name="p3961mcpsimp"></a>n_len</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p3963mcpsimp"><a name="p3963mcpsimp"></a><a name="p3963mcpsimp"></a>RSA公钥N的长度</p>
</td>
</tr>
<tr id="row3964mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p3966mcpsimp"><a name="p3966mcpsimp"></a><a name="p3966mcpsimp"></a>e_len</p>
</td>
<td class="cellrowborder" valign="top" width="70%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p3968mcpsimp"><a name="p3968mcpsimp"></a><a name="p3968mcpsimp"></a>RSA公钥E的长度</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

n、e不能为空。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_rsa\_public\_encrypt](#ss_mpi_cipher_rsa_public_encrypt)
-   [ss\_mpi\_cipher\_rsa\_public\_decrypt](#ss_mpi_cipher_rsa_public_decrypt)
-   [ss\_mpi\_cipher\_rsa\_verify](#ss_mpi_cipher_rsa_verify)

## ot\_cipher\_rsa\_private\_key<a name="ZH-CN_TOPIC_0000002441653077"></a>

【说明】

定义RSA私钥结构体。

【定义】

```
/* RSA private key struct */
typedef struct {
    td_u8 *n;         /* Pub modulus    */
    td_u8 *e;         /* Pub exponent   */
    td_u8 *d;         /* Private exponent  */
    td_u8 *p;         /* 1st prime factor  */
    td_u8 *q;         /* 2nd prime factor  */
    td_u8 *dp;        /* d % (p - 1) */
    td_u8 *dq;        /* d % (q - 1) */
    td_u8 *qp;        /* 1 / (q % p) */
    td_u16 n_len;     /* Length of pub modulus */
    td_u16 e_len;     /* Length of pub exponent */
    td_u16 d_len;     /* Length of private exponent */
    td_u16 p_len;
    td_u16 q_len;
    td_u16 dp_len;
    td_u16 dq_len;
    td_u16 qp_len;
} ot_cipher_rsa_private_key;
```

【成员】

<a name="table4004mcpsimp"></a>
<table><thead align="left"><tr id="row4009mcpsimp"><th class="cellrowborder" valign="top" width="48%" id="mcps1.1.3.1.1"><p id="p4011mcpsimp"><a name="p4011mcpsimp"></a><a name="p4011mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="52%" id="mcps1.1.3.1.2"><p id="p4013mcpsimp"><a name="p4013mcpsimp"></a><a name="p4013mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4015mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4017mcpsimp"><a name="p4017mcpsimp"></a><a name="p4017mcpsimp"></a>n</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p id="p4019mcpsimp"><a name="p4019mcpsimp"></a><a name="p4019mcpsimp"></a>指向RSA私钥n的指针</p>
</td>
</tr>
<tr id="row4020mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4022mcpsimp"><a name="p4022mcpsimp"></a><a name="p4022mcpsimp"></a>e</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4024mcpsimp"><a name="p4024mcpsimp"></a><a name="p4024mcpsimp"></a>指向RSA私钥e的指针</p>
</td>
</tr>
<tr id="row4025mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4027mcpsimp"><a name="p4027mcpsimp"></a><a name="p4027mcpsimp"></a>d</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4029mcpsimp"><a name="p4029mcpsimp"></a><a name="p4029mcpsimp"></a>指向RSA私钥d的指针</p>
</td>
</tr>
<tr id="row4030mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4032mcpsimp"><a name="p4032mcpsimp"></a><a name="p4032mcpsimp"></a>p</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4034mcpsimp"><a name="p4034mcpsimp"></a><a name="p4034mcpsimp"></a>指向RSA私钥p的指针</p>
</td>
</tr>
<tr id="row4035mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4037mcpsimp"><a name="p4037mcpsimp"></a><a name="p4037mcpsimp"></a>q</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4039mcpsimp"><a name="p4039mcpsimp"></a><a name="p4039mcpsimp"></a>指向RSA私钥q的指针</p>
</td>
</tr>
<tr id="row4040mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4042mcpsimp"><a name="p4042mcpsimp"></a><a name="p4042mcpsimp"></a>dp</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4044mcpsimp"><a name="p4044mcpsimp"></a><a name="p4044mcpsimp"></a>指向RSA私钥dp的指针</p>
</td>
</tr>
<tr id="row4045mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4047mcpsimp"><a name="p4047mcpsimp"></a><a name="p4047mcpsimp"></a>dq</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4049mcpsimp"><a name="p4049mcpsimp"></a><a name="p4049mcpsimp"></a>指向RSA私钥dq的指针</p>
</td>
</tr>
<tr id="row4050mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4052mcpsimp"><a name="p4052mcpsimp"></a><a name="p4052mcpsimp"></a>qp</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4054mcpsimp"><a name="p4054mcpsimp"></a><a name="p4054mcpsimp"></a>指向RSA私钥qp的指针</p>
</td>
</tr>
<tr id="row4055mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4057mcpsimp"><a name="p4057mcpsimp"></a><a name="p4057mcpsimp"></a>n_len</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4059mcpsimp"><a name="p4059mcpsimp"></a><a name="p4059mcpsimp"></a>RSA私钥n的长度</p>
</td>
</tr>
<tr id="row4060mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4062mcpsimp"><a name="p4062mcpsimp"></a><a name="p4062mcpsimp"></a>e_len</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4064mcpsimp"><a name="p4064mcpsimp"></a><a name="p4064mcpsimp"></a>RSA私钥e的长度</p>
</td>
</tr>
<tr id="row4065mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4067mcpsimp"><a name="p4067mcpsimp"></a><a name="p4067mcpsimp"></a>d_len</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4069mcpsimp"><a name="p4069mcpsimp"></a><a name="p4069mcpsimp"></a>RSA私钥d的长度</p>
</td>
</tr>
<tr id="row4070mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4072mcpsimp"><a name="p4072mcpsimp"></a><a name="p4072mcpsimp"></a>p_len</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4074mcpsimp"><a name="p4074mcpsimp"></a><a name="p4074mcpsimp"></a>RSA私钥p的长度，长度为n_len一半</p>
</td>
</tr>
<tr id="row4075mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4077mcpsimp"><a name="p4077mcpsimp"></a><a name="p4077mcpsimp"></a>q_len</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4079mcpsimp"><a name="p4079mcpsimp"></a><a name="p4079mcpsimp"></a>RSA私钥q的长度，长度为n_len一半</p>
</td>
</tr>
<tr id="row4080mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4082mcpsimp"><a name="p4082mcpsimp"></a><a name="p4082mcpsimp"></a>dp_len</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4084mcpsimp"><a name="p4084mcpsimp"></a><a name="p4084mcpsimp"></a>RSA私钥dp的长度，长度为n_len一半</p>
</td>
</tr>
<tr id="row4085mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4087mcpsimp"><a name="p4087mcpsimp"></a><a name="p4087mcpsimp"></a>dq_len</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4089mcpsimp"><a name="p4089mcpsimp"></a><a name="p4089mcpsimp"></a>RSA私钥dq的长度，长度为n_len一半</p>
</td>
</tr>
<tr id="row4090mcpsimp"><td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4092mcpsimp"><a name="p4092mcpsimp"></a><a name="p4092mcpsimp"></a>qp_len</p>
</td>
<td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4094mcpsimp"><a name="p4094mcpsimp"></a><a name="p4094mcpsimp"></a>RSA私钥qp的长度，长度为n_len一半</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

-   n不能为空。
-   d为非空时，e、p、q、dp、dq、qp可以为空；d为空时，p、q、dp、dq、qp不能为空。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_rsa\_private\_encrypt](#ss_mpi_cipher_rsa_private_encrypt)
-   [ss\_mpi\_cipher\_rsa\_private\_decrypt](#ss_mpi_cipher_rsa_private_decrypt)
-   [ss\_mpi\_cipher\_rsa\_sign](#ss_mpi_cipher_rsa_sign)

## ot\_cipher\_sign\_type<a name="ZH-CN_TOPIC_0000002441572853"></a>

【说明】

定义非对称算法签名验签输入数据类型。

【定义】

```
typedef enum {
    OT_CIPHER_SIGN_TYPE_MSG = 0x00,
    OT_CIPHER_SIGN_TYPE_HASH,
    OT_CIPHER_SIGN_TYPE_BUTT,
} ot_cipher_sign_type;
```

【成员】

<a name="table4118mcpsimp"></a>
<table><thead align="left"><tr id="row4123mcpsimp"><th class="cellrowborder" valign="top" width="46%" id="mcps1.1.3.1.1"><p id="p4125mcpsimp"><a name="p4125mcpsimp"></a><a name="p4125mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="54%" id="mcps1.1.3.1.2"><p id="p4127mcpsimp"><a name="p4127mcpsimp"></a><a name="p4127mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4129mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4131mcpsimp"><a name="p4131mcpsimp"></a><a name="p4131mcpsimp"></a>OT_CIPHER_SIGN_TYPE_MSG</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p id="p4133mcpsimp"><a name="p4133mcpsimp"></a><a name="p4133mcpsimp"></a>签名的原数据</p>
</td>
</tr>
<tr id="row4134mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4136mcpsimp"><a name="p4136mcpsimp"></a><a name="p4136mcpsimp"></a>OT_CIPHER_SIGN_TYPE_HASH</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4138mcpsimp"><a name="p4138mcpsimp"></a><a name="p4138mcpsimp"></a>签名的原数据经过摘要算法预处理后的数据</p>
</td>
</tr>
<tr id="row4139mcpsimp"><td class="cellrowborder" valign="top" width="46%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4141mcpsimp"><a name="p4141mcpsimp"></a><a name="p4141mcpsimp"></a>OT_CIPHER_SIGN_TYPE_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="54%" headers="mcps1.1.3.1.2 "><p xml:lang="de-DE" id="p4143mcpsimp"><a name="p4143mcpsimp"></a><a name="p4143mcpsimp"></a>边界值，做边界检查使用，无效签名类型。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

-   对于RSA算法，既支持OT\_CIPHER\_SIGN\_TYPE\_MSG，也支持OT\_CIPHER\_SIGN\_TYPE\_HASH。
-   对于SM2算法，当前仅支持OT\_CIPHER\_SIGN\_TYPE\_MSG。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_rsa\_sign](#ss_mpi_cipher_rsa_sign)
-   [ss\_mpi\_cipher\_rsa\_verify](#ss_mpi_cipher_rsa_verify)
-   [ss\_mpi\_cipher\_sm2\_sign](#ss_mpi_cipher_sm2_sign)
-   [ss\_mpi\_cipher\_sm2\_verify](#ss_mpi_cipher_sm2_verify)

## ot\_cipher\_sign\_in\_data<a name="ZH-CN_TOPIC_0000002408093714"></a>

【说明】

定义非对称算法签名验签输入数据结构体。

【定义】

```
typedef struct {
    ot_cipher_sign_type sign_type;
    td_u8 *input;
    td_u32 input_len;
} ot_cipher_sign_in_data;
```

【成员】

<a name="table4175mcpsimp"></a>
<table><thead align="left"><tr id="row4180mcpsimp"><th class="cellrowborder" valign="top" width="39%" id="mcps1.1.3.1.1"><p id="p4182mcpsimp"><a name="p4182mcpsimp"></a><a name="p4182mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.3.1.2"><p id="p4184mcpsimp"><a name="p4184mcpsimp"></a><a name="p4184mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4186mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4188mcpsimp"><a name="p4188mcpsimp"></a><a name="p4188mcpsimp"></a>sign_type</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4190mcpsimp"><a name="p4190mcpsimp"></a><a name="p4190mcpsimp"></a>签名验签数据类型。</p>
</td>
</tr>
<tr id="row4191mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4193mcpsimp"><a name="p4193mcpsimp"></a><a name="p4193mcpsimp"></a>input</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4195mcpsimp"><a name="p4195mcpsimp"></a><a name="p4195mcpsimp"></a>签名验签输入的数据。</p>
</td>
</tr>
<tr id="row4196mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4198mcpsimp"><a name="p4198mcpsimp"></a><a name="p4198mcpsimp"></a>input_len</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4200mcpsimp"><a name="p4200mcpsimp"></a><a name="p4200mcpsimp"></a>签名验签输入的数据长度<span xml:lang="de-DE" id="ph4201mcpsimp"><a name="ph4201mcpsimp"></a><a name="ph4201mcpsimp"></a>（单位：byte）。</span></p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_rsa\_sign](#ss_mpi_cipher_rsa_sign)
-   [ss\_mpi\_cipher\_rsa\_verify](#ss_mpi_cipher_rsa_verify)
-   [ss\_mpi\_cipher\_sm2\_sign](#ss_mpi_cipher_sm2_sign)
-   [ss\_mpi\_cipher\_sm2\_verify](#ss_mpi_cipher_sm2_verify)

## ot\_cipher\_sm2\_public\_key<a name="ZH-CN_TOPIC_0000002408093742"></a>

【说明】

定义SM2公钥结构体。

【定义】

```
typedef struct {
    td_u32 px[OT_CIPHER_SM2_LEN_IN_WORD];
    td_u32 py[OT_CIPHER_SM2_LEN_IN_WORD];
} ot_cipher_sm2_public_key;
```

【成员】

<a name="table4230mcpsimp"></a>
<table><thead align="left"><tr id="row4235mcpsimp"><th class="cellrowborder" valign="top" width="39%" id="mcps1.1.3.1.1"><p id="p4237mcpsimp"><a name="p4237mcpsimp"></a><a name="p4237mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.3.1.2"><p id="p4239mcpsimp"><a name="p4239mcpsimp"></a><a name="p4239mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4241mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4243mcpsimp"><a name="p4243mcpsimp"></a><a name="p4243mcpsimp"></a>px</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4245mcpsimp"><a name="p4245mcpsimp"></a><a name="p4245mcpsimp"></a>公钥点p的x轴坐标</p>
</td>
</tr>
<tr id="row4246mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4248mcpsimp"><a name="p4248mcpsimp"></a><a name="p4248mcpsimp"></a>py</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4250mcpsimp"><a name="p4250mcpsimp"></a><a name="p4250mcpsimp"></a>公钥点p的y轴坐标</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

SS928V100、SS626V100不支持SM2。

【相关数据类型及接口】

[ss\_mpi\_cipher\_sm2\_encrypt](#ss_mpi_cipher_sm2_encrypt)

## ot\_cipher\_sm2\_private\_key<a name="ZH-CN_TOPIC_0000002441572841"></a>

【说明】

定义SM2私钥结构体。

【定义】

```
typedef struct {
    td_u32 d[OT_CIPHER_SM2_LEN_IN_WORD];
} ot_cipher_sm2_private_key;
```

【成员】

<a name="table4268mcpsimp"></a>
<table><thead align="left"><tr id="row4273mcpsimp"><th class="cellrowborder" valign="top" width="39%" id="mcps1.1.3.1.1"><p id="p4275mcpsimp"><a name="p4275mcpsimp"></a><a name="p4275mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.3.1.2"><p id="p4277mcpsimp"><a name="p4277mcpsimp"></a><a name="p4277mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4279mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4281mcpsimp"><a name="p4281mcpsimp"></a><a name="p4281mcpsimp"></a>d</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4283mcpsimp"><a name="p4283mcpsimp"></a><a name="p4283mcpsimp"></a>私钥d的数值</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

SS928V100、SS626V100不支持SM2。

【相关数据类型及接口】

[ss\_mpi\_cipher\_sm2\_decrypt](#ss_mpi_cipher_sm2_decrypt)

## ot\_cipher\_sm2\_sign<a name="ZH-CN_TOPIC_0000002441653013"></a>

【说明】

定义SM2签名结构体。

【定义】

```
typedef struct {
    td_u32 d[OT_CIPHER_SM2_LEN_IN_WORD];
    td_u32 px[OT_CIPHER_SM2_LEN_IN_WORD];
    td_u32 py[OT_CIPHER_SM2_LEN_IN_WORD];
    td_u8 *id;
    td_u16 id_len;
} ot_cipher_sm2_sign;
```

【成员】

<a name="table4311mcpsimp"></a>
<table><thead align="left"><tr id="row4316mcpsimp"><th class="cellrowborder" valign="top" width="39%" id="mcps1.1.3.1.1"><p id="p4318mcpsimp"><a name="p4318mcpsimp"></a><a name="p4318mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.3.1.2"><p id="p4320mcpsimp"><a name="p4320mcpsimp"></a><a name="p4320mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4322mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4324mcpsimp"><a name="p4324mcpsimp"></a><a name="p4324mcpsimp"></a>d</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4326mcpsimp"><a name="p4326mcpsimp"></a><a name="p4326mcpsimp"></a>SM2私钥d的数值</p>
</td>
</tr>
<tr id="row4327mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4329mcpsimp"><a name="p4329mcpsimp"></a><a name="p4329mcpsimp"></a>px</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4331mcpsimp"><a name="p4331mcpsimp"></a><a name="p4331mcpsimp"></a>SM2公钥点p的x轴坐标</p>
</td>
</tr>
<tr id="row4332mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4334mcpsimp"><a name="p4334mcpsimp"></a><a name="p4334mcpsimp"></a>py</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4336mcpsimp"><a name="p4336mcpsimp"></a><a name="p4336mcpsimp"></a>SM2公钥点p的y轴坐标</p>
</td>
</tr>
<tr id="row4337mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4339mcpsimp"><a name="p4339mcpsimp"></a><a name="p4339mcpsimp"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4341mcpsimp"><a name="p4341mcpsimp"></a><a name="p4341mcpsimp"></a>SM2签名的身份ID</p>
</td>
</tr>
<tr id="row4342mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4344mcpsimp"><a name="p4344mcpsimp"></a><a name="p4344mcpsimp"></a>id_len</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4346mcpsimp"><a name="p4346mcpsimp"></a><a name="p4346mcpsimp"></a>SM2签名的身份ID长度</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

SS928V100、SS626V100不支持SM2。

【相关数据类型及接口】

[ss\_mpi\_cipher\_sm2\_sign](#ss_mpi_cipher_sm2_sign)

## ot\_cipher\_sm2\_verify<a name="ZH-CN_TOPIC_0000002441572885"></a>

【说明】

定义SM2验签结构体。

【定义】

```
typedef struct {
    td_u32 px[OT_CIPHER_SM2_LEN_IN_WORD];
    td_u32 py[OT_CIPHER_SM2_LEN_IN_WORD];
    td_u8 *id;
    td_u16 id_len;
} ot_cipher_sm2_verify;
```

【成员】

<a name="table4370mcpsimp"></a>
<table><thead align="left"><tr id="row4375mcpsimp"><th class="cellrowborder" valign="top" width="39%" id="mcps1.1.3.1.1"><p id="p4377mcpsimp"><a name="p4377mcpsimp"></a><a name="p4377mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.3.1.2"><p id="p4379mcpsimp"><a name="p4379mcpsimp"></a><a name="p4379mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4381mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4383mcpsimp"><a name="p4383mcpsimp"></a><a name="p4383mcpsimp"></a>px</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4385mcpsimp"><a name="p4385mcpsimp"></a><a name="p4385mcpsimp"></a>SM2公钥点p的x轴坐标</p>
</td>
</tr>
<tr id="row4386mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4388mcpsimp"><a name="p4388mcpsimp"></a><a name="p4388mcpsimp"></a>py</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4390mcpsimp"><a name="p4390mcpsimp"></a><a name="p4390mcpsimp"></a>SM2公钥点p的y轴坐标</p>
</td>
</tr>
<tr id="row4391mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4393mcpsimp"><a name="p4393mcpsimp"></a><a name="p4393mcpsimp"></a>id</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4395mcpsimp"><a name="p4395mcpsimp"></a><a name="p4395mcpsimp"></a>SM2验签的身份ID</p>
</td>
</tr>
<tr id="row4396mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4398mcpsimp"><a name="p4398mcpsimp"></a><a name="p4398mcpsimp"></a>id_len</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4400mcpsimp"><a name="p4400mcpsimp"></a><a name="p4400mcpsimp"></a>SM2验签的身份ID长度</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

SS928V100、SS626V100不支持SM2。

【相关数据类型及接口】

[ss\_mpi\_cipher\_sm2\_verify](#ss_mpi_cipher_sm2_verify)

## ot\_cipher\_sm2\_sign\_data<a name="ZH-CN_TOPIC_0000002441653045"></a>

【说明】

定义SM2签名验签数据结构体。

【定义】

```
typedef struct {
    td_u32 r[OT_CIPHER_SM2_LEN_IN_WORD];
    td_u32 s[OT_CIPHER_SM2_LEN_IN_WORD];
} ot_cipher_sm2_sign_data;
```

【成员】

<a name="table4422mcpsimp"></a>
<table><thead align="left"><tr id="row4427mcpsimp"><th class="cellrowborder" valign="top" width="39%" id="mcps1.1.3.1.1"><p id="p4429mcpsimp"><a name="p4429mcpsimp"></a><a name="p4429mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="61%" id="mcps1.1.3.1.2"><p id="p4431mcpsimp"><a name="p4431mcpsimp"></a><a name="p4431mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4433mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4435mcpsimp"><a name="p4435mcpsimp"></a><a name="p4435mcpsimp"></a>r</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4437mcpsimp"><a name="p4437mcpsimp"></a><a name="p4437mcpsimp"></a>SM2签名的数据值r</p>
</td>
</tr>
<tr id="row4438mcpsimp"><td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4440mcpsimp"><a name="p4440mcpsimp"></a><a name="p4440mcpsimp"></a>s</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.3.1.2 "><p id="p4442mcpsimp"><a name="p4442mcpsimp"></a><a name="p4442mcpsimp"></a>SM2签名的数据值s</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

SS928V100、SS626V100不支持SM2。

【相关数据类型及接口】

-   [ss\_mpi\_cipher\_sm2\_sign](#ss_mpi_cipher_sm2_sign)
-   [ss\_mpi\_cipher\_sm2\_verify](#ss_mpi_cipher_sm2_verify)

## ot\_keyslot\_type<a name="ZH-CN_TOPIC_0000002441572929"></a>

【说明】

keyslot类型枚举值。

【定义】

```
typedef enum {
    OT_KEYSLOT_TYPE_MCIPHER,            /* keyslot is used for mcipher. */
    OT_KEYSLOT_TYPE_BUTT,
} ot_keyslot_type;
```

【成员】

<a name="table4461mcpsimp"></a>
<table><thead align="left"><tr id="row4466mcpsimp"><th class="cellrowborder" valign="top" width="52%" id="mcps1.1.3.1.1"><p id="p4468mcpsimp"><a name="p4468mcpsimp"></a><a name="p4468mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.1.3.1.2"><p id="p4470mcpsimp"><a name="p4470mcpsimp"></a><a name="p4470mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4472mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4474mcpsimp"><a name="p4474mcpsimp"></a><a name="p4474mcpsimp"></a>OT_KEYSLOT_TYPE_MCIPHER</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p4476mcpsimp"><a name="p4476mcpsimp"></a><a name="p4476mcpsimp"></a>keyslot 用于 mcipher。</p>
</td>
</tr>
<tr id="row4477mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4479mcpsimp"><a name="p4479mcpsimp"></a><a name="p4479mcpsimp"></a>OT_KEYSLOT_TYPE_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p4481mcpsimp"><a name="p4481mcpsimp"></a><a name="p4481mcpsimp"></a>边界值，做边界检查使用，无效类型。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

-   [ot\_keyslot\_attr](#ot_keyslot_attr)
-   [ss\_mpi\_keyslot\_create](#ss_mpi_keyslot_create)

## ot\_keyslot\_secure\_mode<a name="ZH-CN_TOPIC_0000002441572873"></a>

【说明】

keyslot安全模式枚举值。

【定义】

```
typedef enum {
    OT_KEYSLOT_SECURE_MODE_NONE = 0x00, /* no secure. */
    OT_KEYSLOT_SECURE_MODE_TEE,         /* tee. */
    OT_KEYSLOT_SECURE_MODE_BUTT,
} ot_keyslot_secure_mode;
```

【成员】

<a name="table4501mcpsimp"></a>
<table><thead align="left"><tr id="row4506mcpsimp"><th class="cellrowborder" valign="top" width="51%" id="mcps1.1.3.1.1"><p id="p4508mcpsimp"><a name="p4508mcpsimp"></a><a name="p4508mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="49%" id="mcps1.1.3.1.2"><p id="p4510mcpsimp"><a name="p4510mcpsimp"></a><a name="p4510mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4512mcpsimp"><td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4514mcpsimp"><a name="p4514mcpsimp"></a><a name="p4514mcpsimp"></a>OT_KEYSLOT_SECURE_MODE_NONE</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.3.1.2 "><p id="p4516mcpsimp"><a name="p4516mcpsimp"></a><a name="p4516mcpsimp"></a>keyslot与非安全CPU绑定。</p>
</td>
</tr>
<tr id="row4517mcpsimp"><td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4519mcpsimp"><a name="p4519mcpsimp"></a><a name="p4519mcpsimp"></a>OT_KEYSLOT_SECURE_MODE_TEE</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.3.1.2 "><p id="p4521mcpsimp"><a name="p4521mcpsimp"></a><a name="p4521mcpsimp"></a>keyslot与安全CPU绑定。</p>
</td>
</tr>
<tr id="row4522mcpsimp"><td class="cellrowborder" valign="top" width="51%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4524mcpsimp"><a name="p4524mcpsimp"></a><a name="p4524mcpsimp"></a>OT_KEYSLOT_SECURE_MODE_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="49%" headers="mcps1.1.3.1.2 "><p id="p4526mcpsimp"><a name="p4526mcpsimp"></a><a name="p4526mcpsimp"></a>边界值，做边界检查使用，无效安全模式。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

非安全CPU不能绑定TEE安全模式，安全CPU可绑定非安模式。

【相关数据类型及接口】

-   [ot\_keyslot\_attr](#ot_keyslot_attr)
-   [ss\_mpi\_keyslot\_create](#ss_mpi_keyslot_create)

## ot\_keyslot\_attr<a name="ZH-CN_TOPIC_0000002408093730"></a>

【说明】

keyslot属性结构体。

【定义】

```
typedef struct {
    ot_keyslot_type type;
    ot_keyslot_secure_mode secure_mode;
} ot_keyslot_attr;
```

【成员】

<a name="table4548mcpsimp"></a>
<table><thead align="left"><tr id="row4553mcpsimp"><th class="cellrowborder" valign="top" width="52%" id="mcps1.1.3.1.1"><p id="p4555mcpsimp"><a name="p4555mcpsimp"></a><a name="p4555mcpsimp"></a>成员名称</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.1.3.1.2"><p id="p4557mcpsimp"><a name="p4557mcpsimp"></a><a name="p4557mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4559mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4561mcpsimp"><a name="p4561mcpsimp"></a><a name="p4561mcpsimp"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p4563mcpsimp"><a name="p4563mcpsimp"></a><a name="p4563mcpsimp"></a>keyslot类型。</p>
</td>
</tr>
<tr id="row4564mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p xml:lang="de-DE" id="p4566mcpsimp"><a name="p4566mcpsimp"></a><a name="p4566mcpsimp"></a>secure_mode</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p4568mcpsimp"><a name="p4568mcpsimp"></a><a name="p4568mcpsimp"></a>keyslot安全模式。</p>
</td>
</tr>
</tbody>
</table>

【注意事项】

无。

【相关数据类型及接口】

[ss\_mpi\_keyslot\_create](#ss_mpi_keyslot_create)

## OT\_CIPHER\_MAX\_IV\_SIZE\_IN\_WORD<a name="ZH-CN_TOPIC_0000002441652981"></a>

【说明】

CIPHER 的IV最大长度。

【定义】

```
#define OT_CIPHER_MAX_IV_SIZE_IN_WORD  4
```

【注意事项】

无。

【相关数据类型及接口】

-   [ot\_cipher\_ctrl\_aes](#ot_cipher_ctrl_aes)
-   [ot\_cipher\_ctrl\_aes\_ccm\_gcm](#ot_cipher_ctrl_aes_ccm_gcm)
-   [ot\_cipher\_ctrl\_sm4](#ot_cipher_ctrl_sm4)
-   [ot\_cipher\_ctrl](#ot_cipher_ctrl)
-   [ss\_mpi\_cipher\_set\_cfg](#ss_mpi_cipher_set_cfg)
-   [ss\_mpi\_cipher\_get\_cfg](#ss_mpi_cipher_get_cfg)

## OT\_CIPHER\_SM2\_LEN\_IN\_WORD<a name="ZH-CN_TOPIC_0000002408093698"></a>

【说明】

SM2密钥、签名验签数据长度。

【定义】

```
#define OT_CIPHER_SM2_LEN_IN_WORD           8
```

【注意事项】

无。

【相关数据类型及接口】

-   [ot\_cipher\_sm2\_public\_key](#ot_cipher_sm2_public_key)
-   [ot\_cipher\_sm2\_private\_key](#ot_cipher_sm2_private_key)
-   [ot\_cipher\_sm2\_sign](#ot_cipher_sm2_sign)
-   [ot\_cipher\_sm2\_verify](#ot_cipher_sm2_verify)
-   [ot\_cipher\_sm2\_sign\_data](#ot_cipher_sm2_sign_data)

# 错误码
CIPHER提供的错误码如下所示。

**表 1**  CIPHER模块的错误码

<a name="_Ref448994233"></a>
<table><thead align="left"><tr id="row4626mcpsimp"><th class="cellrowborder" valign="top" width="18.81%" id="mcps1.2.4.1.1"><p id="p4628mcpsimp"><a name="p4628mcpsimp"></a><a name="p4628mcpsimp"></a>错误代码</p>
</th>
<th class="cellrowborder" valign="top" width="56.44%" id="mcps1.2.4.1.2"><p id="p4630mcpsimp"><a name="p4630mcpsimp"></a><a name="p4630mcpsimp"></a>宏定义</p>
</th>
<th class="cellrowborder" valign="top" width="24.75%" id="mcps1.2.4.1.3"><p id="p4632mcpsimp"><a name="p4632mcpsimp"></a><a name="p4632mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4634mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4636mcpsimp"><a name="p4636mcpsimp"></a><a name="p4636mcpsimp"></a>0x804d0001</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p xml:lang="pt-BR" id="p4638mcpsimp"><a name="p4638mcpsimp"></a><a name="p4638mcpsimp"></a>OT_ERR_CIPHER_NOT_INIT</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4640mcpsimp"><a name="p4640mcpsimp"></a><a name="p4640mcpsimp"></a>设备未初始化</p>
</td>
</tr>
<tr id="row4641mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4643mcpsimp"><a name="p4643mcpsimp"></a><a name="p4643mcpsimp"></a>0x804d0002</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4645mcpsimp"><a name="p4645mcpsimp"></a><a name="p4645mcpsimp"></a>OT_ERR_CIPHER_INVALID_HANDLE</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4647mcpsimp"><a name="p4647mcpsimp"></a><a name="p4647mcpsimp"></a>Handle号无效</p>
</td>
</tr>
<tr id="row4648mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4650mcpsimp"><a name="p4650mcpsimp"></a><a name="p4650mcpsimp"></a>0x804d0003</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4652mcpsimp"><a name="p4652mcpsimp"></a><a name="p4652mcpsimp"></a>OT_ERR_CIPHER_INVALID_POINT</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4654mcpsimp"><a name="p4654mcpsimp"></a><a name="p4654mcpsimp"></a>参数中有空指针</p>
</td>
</tr>
<tr id="row4655mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4657mcpsimp"><a name="p4657mcpsimp"></a><a name="p4657mcpsimp"></a>0x804d0004</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4659mcpsimp"><a name="p4659mcpsimp"></a><a name="p4659mcpsimp"></a>OT_ERR_CIPHER_INVALID_PARAM</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4661mcpsimp"><a name="p4661mcpsimp"></a><a name="p4661mcpsimp"></a>无效参数</p>
</td>
</tr>
<tr id="row4662mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4664mcpsimp"><a name="p4664mcpsimp"></a><a name="p4664mcpsimp"></a>0x804d0005</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4666mcpsimp"><a name="p4666mcpsimp"></a><a name="p4666mcpsimp"></a>OT_ERR_CIPHER_FAILED_INIT</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4668mcpsimp"><a name="p4668mcpsimp"></a><a name="p4668mcpsimp"></a>初始化失败</p>
</td>
</tr>
<tr id="row4669mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4671mcpsimp"><a name="p4671mcpsimp"></a><a name="p4671mcpsimp"></a>0x804d0006</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4673mcpsimp"><a name="p4673mcpsimp"></a><a name="p4673mcpsimp"></a>OT_ERR_CIPHER_FAILED_GETHANDLE</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4675mcpsimp"><a name="p4675mcpsimp"></a><a name="p4675mcpsimp"></a>获取handle失败</p>
</td>
</tr>
<tr id="row4676mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4678mcpsimp"><a name="p4678mcpsimp"></a><a name="p4678mcpsimp"></a>0x804d0007</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p xml:lang="pt-BR" id="p4680mcpsimp"><a name="p4680mcpsimp"></a><a name="p4680mcpsimp"></a>OT_ERR_CIPHER_FAILED_RELEASEHANDLE</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4682mcpsimp"><a name="p4682mcpsimp"></a><a name="p4682mcpsimp"></a>释放handle失败</p>
</td>
</tr>
<tr id="row4683mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4685mcpsimp"><a name="p4685mcpsimp"></a><a name="p4685mcpsimp"></a>0x804d0008</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4687mcpsimp"><a name="p4687mcpsimp"></a><a name="p4687mcpsimp"></a>OT_ERR_CIPHER_FAILED_CFG_AES</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4689mcpsimp"><a name="p4689mcpsimp"></a><a name="p4689mcpsimp"></a>AES配置无效</p>
</td>
</tr>
<tr id="row4690mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4692mcpsimp"><a name="p4692mcpsimp"></a><a name="p4692mcpsimp"></a>0x804d0009</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4694mcpsimp"><a name="p4694mcpsimp"></a><a name="p4694mcpsimp"></a>OT_ERR_CIPHER_FAILED_CFG_DES</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4696mcpsimp"><a name="p4696mcpsimp"></a><a name="p4696mcpsimp"></a>DES配置无效</p>
</td>
</tr>
<tr id="row4697mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4699mcpsimp"><a name="p4699mcpsimp"></a><a name="p4699mcpsimp"></a>0x804d000a</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4701mcpsimp"><a name="p4701mcpsimp"></a><a name="p4701mcpsimp"></a>OT_ERR_CIPHER_FAILED_ENCRYPT</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4703mcpsimp"><a name="p4703mcpsimp"></a><a name="p4703mcpsimp"></a>加密失败</p>
</td>
</tr>
<tr id="row4704mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4706mcpsimp"><a name="p4706mcpsimp"></a><a name="p4706mcpsimp"></a>0x804d000b</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4708mcpsimp"><a name="p4708mcpsimp"></a><a name="p4708mcpsimp"></a>OT_ERR_CIPHER_FAILED_DECRYPT</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4710mcpsimp"><a name="p4710mcpsimp"></a><a name="p4710mcpsimp"></a>解密失败</p>
</td>
</tr>
<tr id="row4711mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4713mcpsimp"><a name="p4713mcpsimp"></a><a name="p4713mcpsimp"></a>0x804d000c</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4715mcpsimp"><a name="p4715mcpsimp"></a><a name="p4715mcpsimp"></a>OT_ERR_CIPHER_BUSY</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4717mcpsimp"><a name="p4717mcpsimp"></a><a name="p4717mcpsimp"></a>忙状态</p>
</td>
</tr>
<tr id="row4718mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4720mcpsimp"><a name="p4720mcpsimp"></a><a name="p4720mcpsimp"></a>0x804d000d</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p xml:lang="pt-BR" id="p4722mcpsimp"><a name="p4722mcpsimp"></a><a name="p4722mcpsimp"></a>OT_ERR_CIPHER_NO_AVAILABLE_RNG</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4724mcpsimp"><a name="p4724mcpsimp"></a><a name="p4724mcpsimp"></a>没有可用的随机数</p>
</td>
</tr>
<tr id="row4725mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4727mcpsimp"><a name="p4727mcpsimp"></a><a name="p4727mcpsimp"></a>0x804d000e</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4729mcpsimp"><a name="p4729mcpsimp"></a><a name="p4729mcpsimp"></a>OT_ERR_CIPHER_FAILED_MEM</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4731mcpsimp"><a name="p4731mcpsimp"></a><a name="p4731mcpsimp"></a>内存申请错误</p>
</td>
</tr>
<tr id="row4732mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4734mcpsimp"><a name="p4734mcpsimp"></a><a name="p4734mcpsimp"></a>0x804d000f</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4736mcpsimp"><a name="p4736mcpsimp"></a><a name="p4736mcpsimp"></a>OT_ERR_CIPHER_UNAVAILABLE</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4738mcpsimp"><a name="p4738mcpsimp"></a><a name="p4738mcpsimp"></a>不可用</p>
</td>
</tr>
<tr id="row4739mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4741mcpsimp"><a name="p4741mcpsimp"></a><a name="p4741mcpsimp"></a>0x804d0010</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4743mcpsimp"><a name="p4743mcpsimp"></a><a name="p4743mcpsimp"></a>OT_ERR_CIPHER_OVERFLOW</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4745mcpsimp"><a name="p4745mcpsimp"></a><a name="p4745mcpsimp"></a>数据溢出</p>
</td>
</tr>
<tr id="row4746mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4748mcpsimp"><a name="p4748mcpsimp"></a><a name="p4748mcpsimp"></a>0x804d0011</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4750mcpsimp"><a name="p4750mcpsimp"></a><a name="p4750mcpsimp"></a>OT_ERR_CIPHER_HARD_STATUS</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4752mcpsimp"><a name="p4752mcpsimp"></a><a name="p4752mcpsimp"></a>硬件状态错误</p>
</td>
</tr>
<tr id="row4753mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4755mcpsimp"><a name="p4755mcpsimp"></a><a name="p4755mcpsimp"></a>0x804d0012</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4757mcpsimp"><a name="p4757mcpsimp"></a><a name="p4757mcpsimp"></a>OT_ERR_CIPHER_TIMEOUT</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4759mcpsimp"><a name="p4759mcpsimp"></a><a name="p4759mcpsimp"></a>等待超时</p>
</td>
</tr>
<tr id="row4760mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4762mcpsimp"><a name="p4762mcpsimp"></a><a name="p4762mcpsimp"></a>0x804d0013</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4764mcpsimp"><a name="p4764mcpsimp"></a><a name="p4764mcpsimp"></a>OT_ERR_CIPHER_UNSUPPORTED</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4766mcpsimp"><a name="p4766mcpsimp"></a><a name="p4766mcpsimp"></a>不支持的配置</p>
</td>
</tr>
<tr id="row4767mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4769mcpsimp"><a name="p4769mcpsimp"></a><a name="p4769mcpsimp"></a>0x804d0014</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p xml:lang="pt-BR" id="p4771mcpsimp"><a name="p4771mcpsimp"></a><a name="p4771mcpsimp"></a>OT_ERR_CIPHER_REGISTER_IRQ</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4773mcpsimp"><a name="p4773mcpsimp"></a><a name="p4773mcpsimp"></a>中断号无效</p>
</td>
</tr>
<tr id="row4774mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4776mcpsimp"><a name="p4776mcpsimp"></a><a name="p4776mcpsimp"></a>0x804d0015</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4778mcpsimp"><a name="p4778mcpsimp"></a><a name="p4778mcpsimp"></a>OT_ERR_CIPHER_ILLEGAL_UUID</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4780mcpsimp"><a name="p4780mcpsimp"></a><a name="p4780mcpsimp"></a>非法UUID</p>
</td>
</tr>
<tr id="row4781mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4783mcpsimp"><a name="p4783mcpsimp"></a><a name="p4783mcpsimp"></a>0x804d0016</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4785mcpsimp"><a name="p4785mcpsimp"></a><a name="p4785mcpsimp"></a>OT_ERR_CIPHER_ILLEGAL_KEY</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4787mcpsimp"><a name="p4787mcpsimp"></a><a name="p4787mcpsimp"></a>非法key</p>
</td>
</tr>
<tr id="row4788mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4790mcpsimp"><a name="p4790mcpsimp"></a><a name="p4790mcpsimp"></a>0x804d0017</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4792mcpsimp"><a name="p4792mcpsimp"></a><a name="p4792mcpsimp"></a>OT_ERR_CIPHER_INVALID_ADDR</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4794mcpsimp"><a name="p4794mcpsimp"></a><a name="p4794mcpsimp"></a>无效地址</p>
</td>
</tr>
<tr id="row4795mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4797mcpsimp"><a name="p4797mcpsimp"></a><a name="p4797mcpsimp"></a>0x804d0018</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4799mcpsimp"><a name="p4799mcpsimp"></a><a name="p4799mcpsimp"></a>OT_ERR_CIPHER_INVALID_LEN</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4801mcpsimp"><a name="p4801mcpsimp"></a><a name="p4801mcpsimp"></a>无效长度</p>
</td>
</tr>
<tr id="row4802mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4804mcpsimp"><a name="p4804mcpsimp"></a><a name="p4804mcpsimp"></a>0x804d0019</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4806mcpsimp"><a name="p4806mcpsimp"></a><a name="p4806mcpsimp"></a>OT_ERR_CIPHER_ILLEGAL_DATA</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4808mcpsimp"><a name="p4808mcpsimp"></a><a name="p4808mcpsimp"></a>无效数据</p>
</td>
</tr>
<tr id="row4809mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4811mcpsimp"><a name="p4811mcpsimp"></a><a name="p4811mcpsimp"></a>0x804d001a</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4813mcpsimp"><a name="p4813mcpsimp"></a><a name="p4813mcpsimp"></a>OT_ERR_CIPHER_RSA_SIGN</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4815mcpsimp"><a name="p4815mcpsimp"></a><a name="p4815mcpsimp"></a>RSA签名失败</p>
</td>
</tr>
<tr id="row4816mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4818mcpsimp"><a name="p4818mcpsimp"></a><a name="p4818mcpsimp"></a>0x804d001b</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4820mcpsimp"><a name="p4820mcpsimp"></a><a name="p4820mcpsimp"></a>OT_ERR_CIPHER_RSA_VERIFY</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4822mcpsimp"><a name="p4822mcpsimp"></a><a name="p4822mcpsimp"></a>RSA校验失败</p>
</td>
</tr>
<tr id="row4823mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4825mcpsimp"><a name="p4825mcpsimp"></a><a name="p4825mcpsimp"></a>0x804d001c</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4827mcpsimp"><a name="p4827mcpsimp"></a><a name="p4827mcpsimp"></a>OT_ERR_CIPHER_FAILED_SEC_FUNC</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4829mcpsimp"><a name="p4829mcpsimp"></a><a name="p4829mcpsimp"></a>调用安全函数失败</p>
</td>
</tr>
<tr id="row4830mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p4832mcpsimp"><a name="p4832mcpsimp"></a><a name="p4832mcpsimp"></a>-1</p>
</td>
<td class="cellrowborder" valign="top" width="56.44%" headers="mcps1.2.4.1.2 "><p id="p4834mcpsimp"><a name="p4834mcpsimp"></a><a name="p4834mcpsimp"></a>TD_FAILURE</p>
</td>
<td class="cellrowborder" valign="top" width="24.75%" headers="mcps1.2.4.1.3 "><p id="p4836mcpsimp"><a name="p4836mcpsimp"></a><a name="p4836mcpsimp"></a>操作失败</p>
</td>
</tr>
</tbody>
</table>

# Proc调试信息
## CIPHER状态<a name="ZH-CN_TOPIC_0000002408093750"></a>

【调试信息】

```
执行 cat /proc/umap/cipher
[CIPHER] Version: [V1.0.0.0 B010 Release], Build Time[Apr  7 2021, 16:08:45]
---------------------------------------- cipher status --------------------
chn_id   status   decrypt   alg    mode   key_len     addr in/out
01     open       0      AES   CCM     128    73cb0004/73cb1004
02     close      0      AES   ECB     000    00000000/00000000
03     close      0      AES   ECB     000    00000000/00000000
04     close      0      AES   ECB     000    00000000/00000000
05     close      0      AES   ECB     000    00000000/00000000
06     close      0      AES   ECB     000    00000000/00000000
07     close      0      AES   ECB     000    00000000/00000000
08     close      0      AES   ECB     000    00000000/00000000
09     close      0      AES   ECB     000    00000000/00000000
10     close      0      AES   ECB     000    00000000/00000000
11     close      0      AES   ECB     000    00000000/00000000
12     close      0      AES   ECB     000    00000000/00000000
13     close      0      AES   ECB     000    00000000/00000000
14     close      0      AES   ECB     000    00000000/00000000
15     close      0      AES   ECB     000    00000000/00000000
---------------------------------------------
key_from   int_raw     int_en   int_status   iv_out
00         0         0         0       07101112050000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
00         0         0         0       00000000000000000000000000000000
```

【调试信息分析】

记录当前CIPHER各个通道的配置信息。

【参数说明】

<a name="table4879mcpsimp"></a>
<table><thead align="left"><tr id="row4885mcpsimp"><th class="cellrowborder" colspan="2" valign="top" id="mcps1.1.4.1.1"><p id="p4887mcpsimp"><a name="p4887mcpsimp"></a><a name="p4887mcpsimp"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" id="mcps1.1.4.1.2"><p id="p4889mcpsimp"><a name="p4889mcpsimp"></a><a name="p4889mcpsimp"></a>描述</p>
</th>
</tr>
</thead>
<tbody><tr id="row4891mcpsimp"><td class="cellrowborder" rowspan="12" valign="top" width="14.000000000000002%" headers="mcps1.1.4.1.1 "><p id="p4893mcpsimp"><a name="p4893mcpsimp"></a><a name="p4893mcpsimp"></a>CIPHER基本属性</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.1.4.1.1 "><p id="p4895mcpsimp"><a name="p4895mcpsimp"></a><a name="p4895mcpsimp"></a>chn_id</p>
</td>
<td class="cellrowborder" valign="top" width="61%" headers="mcps1.1.4.1.2 "><p id="p4897mcpsimp"><a name="p4897mcpsimp"></a><a name="p4897mcpsimp"></a>通道号</p>
</td>
</tr>
<tr id="row4898mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4900mcpsimp"><a name="p4900mcpsimp"></a><a name="p4900mcpsimp"></a>status</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4902mcpsimp"><a name="p4902mcpsimp"></a><a name="p4902mcpsimp"></a>打开/关闭</p>
</td>
</tr>
<tr id="row4903mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4905mcpsimp"><a name="p4905mcpsimp"></a><a name="p4905mcpsimp"></a>decrypt</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4907mcpsimp"><a name="p4907mcpsimp"></a><a name="p4907mcpsimp"></a>加密/解密</p>
</td>
</tr>
<tr id="row4908mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4910mcpsimp"><a name="p4910mcpsimp"></a><a name="p4910mcpsimp"></a>alg</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4912mcpsimp"><a name="p4912mcpsimp"></a><a name="p4912mcpsimp"></a>算法，AES等</p>
</td>
</tr>
<tr id="row4913mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4915mcpsimp"><a name="p4915mcpsimp"></a><a name="p4915mcpsimp"></a>mode</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4917mcpsimp"><a name="p4917mcpsimp"></a><a name="p4917mcpsimp"></a>模式，ECB/CBC/CFB/CTR等</p>
</td>
</tr>
<tr id="row4918mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4920mcpsimp"><a name="p4920mcpsimp"></a><a name="p4920mcpsimp"></a>key_len</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4922mcpsimp"><a name="p4922mcpsimp"></a><a name="p4922mcpsimp"></a>密钥长度，128/192/256等</p>
</td>
</tr>
<tr id="row4923mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4925mcpsimp"><a name="p4925mcpsimp"></a><a name="p4925mcpsimp"></a>addr in/out</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4927mcpsimp"><a name="p4927mcpsimp"></a><a name="p4927mcpsimp"></a>输入/输出物理地址</p>
</td>
</tr>
<tr id="row4928mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4930mcpsimp"><a name="p4930mcpsimp"></a><a name="p4930mcpsimp"></a>key_from</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4932mcpsimp"><a name="p4932mcpsimp"></a><a name="p4932mcpsimp"></a>密钥来源，KEYSLOT编号</p>
</td>
</tr>
<tr id="row4933mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4935mcpsimp"><a name="p4935mcpsimp"></a><a name="p4935mcpsimp"></a>int_raw</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4937mcpsimp"><a name="p4937mcpsimp"></a><a name="p4937mcpsimp"></a>是否有原始中断</p>
</td>
</tr>
<tr id="row4938mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4940mcpsimp"><a name="p4940mcpsimp"></a><a name="p4940mcpsimp"></a>int_en</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4942mcpsimp"><a name="p4942mcpsimp"></a><a name="p4942mcpsimp"></a>是否中断使能</p>
</td>
</tr>
<tr id="row4943mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4945mcpsimp"><a name="p4945mcpsimp"></a><a name="p4945mcpsimp"></a>int_status</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4947mcpsimp"><a name="p4947mcpsimp"></a><a name="p4947mcpsimp"></a>中断状态</p>
</td>
</tr>
<tr id="row4948mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4950mcpsimp"><a name="p4950mcpsimp"></a><a name="p4950mcpsimp"></a>iv_out</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.4.1.1 "><p id="p4952mcpsimp"><a name="p4952mcpsimp"></a><a name="p4952mcpsimp"></a>输出IV</p>
</td>
</tr>
</tbody>
</table>

