---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/SS928V100╱SS927V100 安全启动使用指南/SS928V100╱SS927V100 安全启动使用指南.md
---

# Preface
**Overview<a name="section236mcpsimp"></a>**

This document is intended to guide personnel using this secure boot solution in understanding the overall security solution process, and then using this secure boot solution through specific operational steps and methods. It mainly introduces the specifications and features of this secure boot, including the basic secure boot flow, the key hierarchy and signature verification logic, and the overall usage of the secure boot solution.

>![](public_sys-resources/icon-note.gif) **Note:**
>This document takes the SS928V100 description as an example. Unless otherwise specified, the content for SS927V100 is identical to that of SS928V100.

**Product Version<a name="section239mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table242mcpsimp"></a>
<table><thead align="left"><tr id="row247mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p249mcpsimp"><a name="p249mcpsimp"></a><a name="p249mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p251mcpsimp"><a name="p251mcpsimp"></a><a name="p251mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row253mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p255mcpsimp"><a name="p255mcpsimp"></a><a name="p255mcpsimp"></a>SS928</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p257mcpsimp"><a name="p257mcpsimp"></a><a name="p257mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row1186319271312"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8648177191319"><a name="p8648177191319"></a><a name="p8648177191319"></a>SS927</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p136484751315"><a name="p136484751315"></a><a name="p136484751315"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section258mcpsimp"></a>**

This document (guide) is mainly applicable to the following engineers:

-   Technical Support Engineer
-   Software Development Engineer

**Symbol Conventions<a name="section133020216410"></a>**

The following symbols may appear in this document, and their meanings are as described below.

<a name="table2622507016410"></a>
<table><thead align="left"><tr id="row1530720816410"><th class="cellrowborder" valign="top" width="20.580000000000002%" id="mcps1.1.3.1.1"><p id="p6450074116410"><a name="p6450074116410"></a><a name="p6450074116410"></a><strong id="b2136615816410"><a name="b2136615816410"></a><a name="b2136615816410"></a>Symbol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="79.42%" id="mcps1.1.3.1.2"><p id="p5435366816410"><a name="p5435366816410"></a><a name="p5435366816410"></a><strong id="b5941558116410"><a name="b5941558116410"></a><a name="b5941558116410"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row1372280416410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p3734547016410"><a name="p3734547016410"></a><a name="p3734547016410"></a><a name="image2670064316410"></a><a name="image2670064316410"></a><span><img class="" id="image2670064316410" height="25.270000000000003" width="67.83" src="/soc-linux/secure-boot/figures/zh-cn_image_0000002457876689.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p1757432116410"><a name="p1757432116410"></a><a name="p1757432116410"></a>Indicates a high-risk hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row466863216410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1432579516410"><a name="p1432579516410"></a><a name="p1432579516410"></a><a name="image4895582316410"></a><a name="image4895582316410"></a><span><img class="" id="image4895582316410" height="25.270000000000003" width="67.83" src="/soc-linux/secure-boot/figures/zh-cn_image_0000002424357782.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p959197916410"><a name="p959197916410"></a><a name="p959197916410"></a>Indicates a medium-risk hazard which, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row123863216410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p1232579516410"><a name="p1232579516410"></a><a name="p1232579516410"></a><a name="image1235582316410"></a><a name="image1235582316410"></a><span><img class="" id="image1235582316410" height="25.270000000000003" width="67.83" src="/soc-linux/secure-boot/figures/zh-cn_image_0000002424197962.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p123197916410"><a name="p123197916410"></a><a name="p123197916410"></a>Indicates a low-risk hazard which, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row5786682116410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p2204984716410"><a name="p2204984716410"></a><a name="p2204984716410"></a><a name="image4504446716410"></a><a name="image4504446716410"></a><span><img class="" id="image4504446716410" height="25.270000000000003" width="67.83" src="/soc-linux/secure-boot/figures/zh-cn_image_0000002457836557.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p4388861916410"><a name="p4388861916410"></a><a name="p4388861916410"></a>Used to convey equipment or environmental safety warning information. Failure to avoid may result in equipment damage, data loss, reduced equipment performance, or other unpredictable consequences.</p>
<p id="p1238861916410"><a name="p1238861916410"></a><a name="p1238861916410"></a>"Caution" does not involve personal injury.</p>
</td>
</tr>
<tr id="row2856923116410"><td class="cellrowborder" valign="top" width="20.580000000000002%" headers="mcps1.1.3.1.1 "><p id="p5555360116410"><a name="p5555360116410"></a><a name="p5555360116410"></a><a name="image799324016410"></a><a name="image799324016410"></a><span><img class="" id="image799324016410" height="25.270000000000003" width="67.83" src="/soc-linux/secure-boot/figures/zh-cn_image_0000002457876693.png"></span></p>
</td>
<td class="cellrowborder" valign="top" width="79.42%" headers="mcps1.1.3.1.2 "><p id="p4612588116410"><a name="p4612588116410"></a><a name="p4612588116410"></a>Supplementary explanation of key information in the main text.</p>
<p id="p1232588116410"><a name="p1232588116410"></a><a name="p1232588116410"></a>"Note" is not a safety warning and does not involve personal, equipment, or environmental hazard information.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section2467512116410"></a>**

<a name="table256mcpsimp"></a>
<table><thead align="left"><tr id="row262mcpsimp"><th class="cellrowborder" valign="top" width="20.97%" id="mcps1.1.4.1.1"><p id="p264mcpsimp"><a name="p264mcpsimp"></a><a name="p264mcpsimp"></a><strong id="b265mcpsimp"><a name="b265mcpsimp"></a><a name="b265mcpsimp"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26.029999999999998%" id="mcps1.1.4.1.2"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a><strong id="b268mcpsimp"><a name="b268mcpsimp"></a><a name="b268mcpsimp"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p270mcpsimp"><a name="p270mcpsimp"></a><a name="p270mcpsimp"></a><strong id="b271mcpsimp"><a name="b271mcpsimp"></a><a name="b271mcpsimp"></a>Revision Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row280mcpsimp"><td class="cellrowborder" valign="top" width="20.97%" headers="mcps1.1.4.1.1 "><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26.029999999999998%" headers="mcps1.1.4.1.2 "><p id="p284mcpsimp"><a name="p284mcpsimp"></a><a name="p284mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p286mcpsimp"><a name="p286mcpsimp"></a><a name="p286mcpsimp"></a>First interim version release.</p>
</td>
</tr>
</tbody>
</table>

# Security Features
The chip provides a variety of rich security features based on a hardware root of trust, meeting the requirements of different application scenarios and security levels, facilitating the implementation and deployment of customer product secure boot solutions. Key features are as follows:

## On-Chip OTP Resources<a name="ZH-CN_TOPIC_0000002457836521"></a>

OTP is a special type of non-volatile memory that allows programming once, with data remaining valid permanently. Leveraging the physical characteristic of one-time programmability, OTP stores irreversible control switches, hardware root keys, etc. The key region provides multiple symmetric root key slots for storing multiple symmetric root keys. The key region can only be programmed once, is automatically locked, and cannot be read back. The status control region and user-defined region can be programmed multiple times, with corresponding bits only changeable from 0 to 1; bits that are already 1 cannot be updated. If the content needs to remain unchangeable after one-time programming, the region can be locked after writing. The version control region can be programmed multiple times, with all bits only changeable from 0 to 1; this is irreversible and cannot be locked.

## Built-in Key Management Module<a name="ZH-CN_TOPIC_0000002424197882"></a>

For each symmetric root key already programmed into the OTP, the key management module performs multi-level derivation based on the corresponding external input (key derivation material), generates the corresponding working key, and directly delivers the working key to the encryption/decryption engine (SPACC) to perform encryption/decryption operations on the final data. The entire key derivation process is completed within the hardware logic. The root key, key protection key, and working key never appear in memory and cannot be read by software, improving key security.

## Built-in Hardware Cryptographic Algorithm Engine<a name="ZH-CN_TOPIC_0000002457876613"></a>

The chip's hardware encryption/decryption algorithm engine supports a variety of common asymmetric cryptographic algorithms, symmetric cryptographic algorithms, and hash algorithms. The secure boot solution uses RSA4096 and SHA256 algorithms for signature verification of images. Secure boot can also support encryption protection of images based on customer requirements, using the AES256 encryption/decryption algorithm.

## Security Trust Chain<a name="ZH-CN_TOPIC_0000002457876657"></a>

The chip supports secure boot based on a hardware root of trust, implementing step-by-step verification starting from the hardware root of trust to ensure the trustworthiness of the boot process. Customers can store the public key hash in OTP, and the chip's BOOTROM completes the integrity and authenticity verification of the root public key, as well as the step-by-step verification of subordinate public keys and images.

## Version Anti-Rollback<a name="ZH-CN_TOPIC_0000002457836505"></a>

A version control region is reserved in the chip's OTP to implement version anti-rollback control during secure boot and secure upgrades, preventing attackers from using a defective historical version to replace a new version and attack the device.

## Unified Image Structure<a name="ZH-CN_TOPIC_0000002457876629"></a>

Secure boot involves multiple keys and signatures that need to be appended to the final image. To avoid various issues introduced by multiple versions during image creation and usage, and to reduce complexity, this boot solution unifies the images used for secure boot and non-secure boot into a single format. When the SoC does not enable secure boot, a non-encrypted secure boot image (with corresponding keys and signatures) can still boot normally.

# Boot Schemes
-   Supports 3 boot schemes: fast boot, non-secure boot, and secure boot.
-   Fast boot has only one level of Bootloader (U-Boot), where U-Boot directly boots Linux.
-   Non-secure boot and secure boot include two levels of Bootloader.
    -   GSL is the primary Bootloader;
    -   U-Boot is the secondary Bootloader, where customers can configure and develop corresponding functions as needed, such as Flash drivers and Linux system boot.

-   [Table 1](#table23618501607) compares the characteristics of each boot scheme, with "√" indicating the scheme has that characteristic, and "-" indicating it does not.

**Table 1** Comparison of Boot Scheme Characteristics

<a name="table23618501607"></a>
<table><thead align="left"><tr id="row1636135010010"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.1"><p id="p55641634115"><a name="p55641634115"></a><a name="p55641634115"></a>Characteristic</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.2"><p id="p17564173515"><a name="p17564173515"></a><a name="p17564173515"></a>Fast Boot</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.3"><p id="p35642034110"><a name="p35642034110"></a><a name="p35642034110"></a>Non-Secure Boot</p>
</th>
<th class="cellrowborder" valign="top" width="25%" id="mcps1.2.5.1.4"><p id="p85651339111"><a name="p85651339111"></a><a name="p85651339111"></a>Secure Boot</p>
</th>
</tr>
</thead>
<tbody><tr id="row1136125012019"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p105651931319"><a name="p105651931319"></a><a name="p105651931319"></a>Uses U-Boot</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p195651431219"><a name="p195651431219"></a><a name="p195651431219"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p135651031118"><a name="p135651031118"></a><a name="p135651031118"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p18565831117"><a name="p18565831117"></a><a name="p18565831117"></a>√</p>
</td>
</tr>
<tr id="row1936110501408"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p9565931017"><a name="p9565931017"></a><a name="p9565931017"></a>Uses GSL</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p25651310114"><a name="p25651310114"></a><a name="p25651310114"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p1656523016"><a name="p1656523016"></a><a name="p1656523016"></a>√</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p45654313116"><a name="p45654313116"></a><a name="p45654313116"></a>√</p>
</td>
</tr>
<tr id="row113620507016"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.1 "><p id="p5565633117"><a name="p5565633117"></a><a name="p5565633117"></a>Decryption & Signature Verification of Images</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.2 "><p id="p9565439117"><a name="p9565439117"></a><a name="p9565439117"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.3 "><p id="p11565203912"><a name="p11565203912"></a><a name="p11565203912"></a>-</p>
</td>
<td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.5.1.4 "><p id="p556563617"><a name="p556563617"></a><a name="p556563617"></a>√</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-notice.gif) **Caution:**
>The boot scheme used by the chip is controlled by OTP. At the factory, the OTP is configured by default for non-secure boot. The boot scheme can be changed by configuring the OTP. For OTP configuration methods, refer to the "[OTP Configuration and Programming](#ZH-CN_TOPIC_0000002457876665)" section below.

## Fast Boot<a name="ZH-CN_TOPIC_0000002457876673"></a>

To be compatible with traditional boot schemes, the chip supports a fast boot scheme. The fast boot flow is shown in [Figure 1](#fig9466924175919), starting directly from U-Boot, which then boots Linux. This scheme does not verify the legitimacy of the boot image and is non-secure. Fast boot is faster than secure boot and non-secure boot and can be used in scenarios where secure boot is not required but speed is.

**Figure 1** Fast Boot Flow<a name="fig9466924175919"></a>
![](figures/快速启动流程.png "快速启动流程")

## Non-Secure Boot<a name="ZH-CN_TOPIC_0000002457836541"></a>

In non-secure boot mode, the chip starts from GSL, with the flow shown in [Figure 1](#fig1746041719160). This scheme does not verify the legitimacy of the boot image and is non-secure.

**Figure 1** Non-Secure Boot Flow<a name="fig1746041719160"></a>
![](figures/非安全启动流程.png "非安全启动流程")

## Secure Boot<a name="ZH-CN_TOPIC_0000002424357722"></a>

Compared with the non-secure boot scheme, the secure boot scheme verifies the legitimacy of the boot image. The scheme is detailed in "[Image Decryption and Signature Verification](#ZH-CN_TOPIC_0000002457836477)". The decryption and verification of images are interdependent at each stage. If verification fails at any intermediate stage, boot fails, thereby ensuring the legitimacy, integrity, and confidentiality of the image.

Secure boot adds image legitimacy verification steps on top of non-secure boot, with the flow shown in [Figure 1](#fig157715217257).

**Figure 1** Secure Boot Flow<a name="fig157715217257"></a>
![](figures/安全启动流程.png "安全启动流程")

>![](public_sys-resources/icon-notice.gif) **Caution:**
>The U-Boot signature verification of Kernel and Rootfs has not been implemented. Customers can refer to "[Reference for Kernel and Filesystem Secure Boot Signature Verification Solution](#ZH-CN_TOPIC_0000002457836481)" and implement it by calling the Cipher API interface based on the application scenario.

# Secure Boot Image Layout and Structure
## Secure Boot Mode Image Layout<a name="ZH-CN_TOPIC_0000002457876641"></a>

The secure boot image on the boot medium is mainly divided into 3 major blocks:

-   The first block is the Boot image, which integrates GSL and U-Boot binary files as well as DDR table content. The layout is shown in [Figure 1](#fig1050352493314).
-   The second block is the Linux kernel.
-   The third block is the filesystem.

**Figure 1** Secure Boot Image Layout Diagram<a name="fig1050352493314"></a>
![](figures/安全启动镜像布局图.png "安全启动镜像布局图")

>![](public_sys-resources/icon-notice.gif) **Caution:**
>Label 1 in the layout diagram: The Boot image area must be placed at the starting address 0x00 of the boot medium. There are no special requirements for the placement of other areas; they can be allocated according to the usage scenario.

## Image Structure Breakdown Diagram<a name="ZH-CN_TOPIC_0000002457836501"></a>

### Vendor\_Root\_Public\_Key Area<a name="ZH-CN_TOPIC_0000002424197922"></a>

Its image distribution diagram is shown in [Figure 1](#fig2809231153619).

**Figure 1** Vendor\_Root\_Public\_Key Area<a name="fig2809231153619"></a>
![](figures/Vendor_Root_Public_Key-Area.png "Vendor_Root_Public_Key-Area")

### OEM\_Root\_Public\_Key Area<a name="ZH-CN_TOPIC_0000002424357734"></a>

Its image distribution diagram is shown in [Figure 1](#fig71661085015).

**Figure 1** OEM\_Root\_Public\_Key Area<a name="fig71661085015"></a>
![](figures/OEM_Root_Public_Key-Area.png "OEM_Root_Public_Key-Area")

### Third\_party\_Root\_Public\_Key Area<a name="ZH-CN_TOPIC_0000002457876617"></a>

Its image distribution diagram is shown in [Figure 1](#fig129062192012).

**Figure 1** Third\_party\_Root\_Public\_Key Area<a name="fig129062192012"></a>
![](figures/Third_party_Root_Public_Key-Area.png "Third_party_Root_Public_Key-Area")

### GSL Flash Mapping<a name="ZH-CN_TOPIC_0000002457836517"></a>

#### GSL third party Key Area<a name="ZH-CN_TOPIC_0000002424197938"></a>

Its image distribution is shown in [Figure 1](#fig065525410618).

**Figure 1** GSL third party Key Area<a name="fig065525410618"></a>
![](figures/GSL-third-party-Key-Area.png "GSL-third-party-Key-Area")

#### GSL Key Area<a name="ZH-CN_TOPIC_0000002424357754"></a>

Its image distribution diagram is shown in [Figure 1](#fig2404758151111).

**Figure 1** GSL Key Area<a name="fig2404758151111"></a>
![](figures/GSL-Key-Area.png "GSL-Key-Area")

#### GSL Code Area<a name="ZH-CN_TOPIC_0000002424197902"></a>

Its image distribution diagram is shown in [Figure 1](#fig9794191161715).

**Figure 1** GSL Code Area<a name="fig9794191161715"></a>
![](figures/GSL-Code-Area.png "GSL-Code-Area")

### Boot Flash Mapping<a name="ZH-CN_TOPIC_0000002457876645"></a>

#### Key Area<a name="ZH-CN_TOPIC_0000002457836529"></a>

Its image distribution diagram is shown in [Figure 1](#fig984510341212).

**Figure 1** Key Area<a name="fig984510341212"></a>
![](figures/Key-Area.png "Key-Area")

#### Params Area<a name="ZH-CN_TOPIC_0000002424197930"></a>

Its image distribution diagram is shown in [Figure 1](#fig488863262618).

**Figure 1** Params Area<a name="fig488863262618"></a>
![](figures/Params-Area.png "Params-Area")

#### Unchecked Area for Vendor<a name="ZH-CN_TOPIC_0000002424357726"></a>

Its image distribution diagram is shown in [Figure 1](#fig148151331193817).

**Figure 1** Unchecked Area for Vendor<a name="fig148151331193817"></a>
![](figures/Unchecked-Area-for-Vendor.png "Unchecked-Area-for-Vendor")

>![](public_sys-resources/icon-notice.gif) **Caution:**
>The SCS\_simulate\_flag is a switch reserved in the "[Boot Flash Mapping](#ZH-CN_TOPIC_0000002457876645)" area for debugging under secure boot. When the OTP corresponding KEY and other information bits have been programmed, but the OTP secure boot flag (field: secure\_boot\_en) is not yet enabled, this flag takes effect. Its purpose is: after the user has programmed OTP without enabling the secure boot flag, this flag can be configured to simulate the secure boot flag being enabled, for debugging the "[Boot Flash Mapping](#ZH-CN_TOPIC_0000002457876645)" area.

#### U-Boot Area<a name="ZH-CN_TOPIC_0000002457876661"></a>

Its image distribution diagram is shown in [Figure 1](#fig1359117512415).

**Figure 1** U-Boot Area<a name="fig1359117512415"></a>
![](figures/U-Boot-Area.png "U-Boot-Area")

# Image Decryption and Signature Verification
This secure boot solution supports integrity verification of images and the use of encrypted images. Whether each level of image is encrypted, and the encryption key used, can be independently controlled. For encrypted images, the boot flow follows the principle of decryption first, then signature verification. The secure boot solution supports a third party performing a secondary signature, providing dual confirmation of image integrity.

According to the "[Secure Boot Image Layout and Structure](#ZH-CN_TOPIC_0000002424197926)", a secure boot image is divided into multiple regions. The data content in each region, along with the encryption/decryption and integrity verification of the data content, is the responsibility of the Owner of that region. The ownership for each region is shown in [Table 1](#table1690721754513).

**Table 1** Region Owners

<a name="table1690721754513"></a>
<table><thead align="left"><tr id="row4907181794511"><th class="cellrowborder" valign="top" width="41.85%" id="mcps1.2.3.1.1"><p id="p1233318245465"><a name="p1233318245465"></a><a name="p1233318245465"></a>Region Name</p>
</th>
<th class="cellrowborder" valign="top" width="58.15%" id="mcps1.2.3.1.2"><p id="p53332024164614"><a name="p53332024164614"></a><a name="p53332024164614"></a>Secure Boot Owner</p>
</th>
</tr>
</thead>
<tbody><tr id="row1290701754511"><td class="cellrowborder" valign="top" width="41.85%" headers="mcps1.2.3.1.1 "><p id="p6334182415468"><a name="p6334182415468"></a><a name="p6334182415468"></a>Vendor_Root_Public_Key Area</p>
</td>
<td class="cellrowborder" valign="top" width="58.15%" headers="mcps1.2.3.1.2 "><p id="p333416241469"><a name="p333416241469"></a><a name="p333416241469"></a>Data invalid in this region</p>
</td>
</tr>
<tr id="row190711717459"><td class="cellrowborder" valign="top" width="41.85%" headers="mcps1.2.3.1.1 "><p id="p19334122414462"><a name="p19334122414462"></a><a name="p19334122414462"></a>OEM_Root_Public_Key Area</p>
</td>
<td class="cellrowborder" valign="top" width="58.15%" headers="mcps1.2.3.1.2 "><p id="p433492414460"><a name="p433492414460"></a><a name="p433492414460"></a>OEM</p>
</td>
</tr>
<tr id="row490810179457"><td class="cellrowborder" valign="top" width="41.85%" headers="mcps1.2.3.1.1 "><p id="p7334124134612"><a name="p7334124134612"></a><a name="p7334124134612"></a>Third_party_Root_Public_Key Area</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="58.15%" headers="mcps1.2.3.1.2 "><p id="p20334424114616"><a name="p20334424114616"></a><a name="p20334424114616"></a>Third party</p>
</td>
</tr>
<tr id="row10548268469"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1333417242463"><a name="p1333417242463"></a><a name="p1333417242463"></a>GSL third party Key Area</p>
</td>
</tr>
<tr id="row191067812469"><td class="cellrowborder" valign="top" width="41.85%" headers="mcps1.2.3.1.1 "><p id="p123343243461"><a name="p123343243461"></a><a name="p123343243461"></a>GSL Key Area</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="58.15%" headers="mcps1.2.3.1.2 "><p id="p2334424154611"><a name="p2334424154611"></a><a name="p2334424154611"></a>OEM</p>
</td>
</tr>
<tr id="row51366954620"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p133492415460"><a name="p133492415460"></a><a name="p133492415460"></a>GSL Code Area</p>
</td>
</tr>
<tr id="row0203101094618"><td class="cellrowborder" valign="top" width="41.85%" headers="mcps1.2.3.1.1 "><p id="p533432474611"><a name="p533432474611"></a><a name="p533432474611"></a>Key Area</p>
</td>
<td class="cellrowborder" rowspan="4" valign="top" width="58.15%" headers="mcps1.2.3.1.2 "><p id="p183348249465"><a name="p183348249465"></a><a name="p183348249465"></a>OEM</p>
</td>
</tr>
<tr id="row127931811134612"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p15334192418465"><a name="p15334192418465"></a><a name="p15334192418465"></a>Params Area</p>
</td>
</tr>
<tr id="row917317143463"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p123340246467"><a name="p123340246467"></a><a name="p123340246467"></a>Uncheck Area for Vendor</p>
</td>
</tr>
<tr id="row19791715174613"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1933452494612"><a name="p1933452494612"></a><a name="p1933452494612"></a>U-Boot Area</p>
</td>
</tr>
</tbody>
</table>

## SoC Secure Boot Public Key Framework<a name="ZH-CN_TOPIC_0000002424197942"></a>

The SoC public key hierarchy architecture design supports starting from the OTP root public key hash during chip boot, performing integrity verification on each level of image, as well as integrity verification on the next level of public key. This achieves trust transfer across all stages of the boot flow. The signature verification for secure boot uses the RSA4096 algorithm and SHA256.

The secure boot solution provides 3 trust chains based on three root public key hashes (stored in OTP). These are Vendor, OEM, and Third Party, with corresponding root public keys being Vendor\_Root\_Public\_Key, OEM\_Root\_Public\_Key, and Third\_party\_Root\_Public\_Key.

In secure boot mode, image signature verification is the responsibility of OEM, with the verification relationship hierarchy shown in [Figure 1](#fig1816828175512).

**Figure 1** Secure Boot Mode Public Key Signature Verification Relationship Diagram<a name="fig1816828175512"></a>
![](figures/安全启动模式公钥验签关系图.png "安全启动模式公钥验签关系图")

## Symmetric Key Management<a name="ZH-CN_TOPIC_0000002457876625"></a>

For secure boot requiring image decryption functionality, the chip's OTP needs to have corresponding symmetric cryptographic algorithm (AES) root keys built in. The chip OTP reserves 4 128-bit root key slots for deriving the corresponding key protection keys and the final working key. Customers can program one or more root keys as needed. Additionally, the chip is pre-configured with a 128-bit Vendor root key stored in a separate OTP space (see Section 2.2 "SSxxxx OTP Field Definitions" in the "Security Subsystem Usage Guide").

### Chip Key Derivation<a name="ZH-CN_TOPIC_0000002457836485"></a>

The SoC provides three levels of key derivation, with its working principle shown in [Figure 1](#fig248010331147). RKP retrieves the root key protected by RKP from OTP (OTP KEY), generates the actual root key within the RKP hardware, and sends it to KLAD through a secure channel. KLAD can perform two levels of key derivation, with each level's key derivation material inputtable from memory. The first-level key derivation material ProtectionKey\_L1 is 128 bits, and the second-level key derivation material ProtectionKey\_L2 is 256 bits. Based on the OTP KEY and key derivation materials, KLAD ultimately outputs the actual working key to the hardware encryption/decryption engine.

**Figure 1** Key Derivation<a name="fig248010331147"></a>
![](figures/密钥派生.png "密钥派生")

### Key Management and Image Decryption in Secure Boot Mode<a name="ZH-CN_TOPIC_0000002457876653"></a>

The symmetric key hierarchy and image decryption relationship for secure boot are shown in [Figure 1](#fig1739414716164).

The root key originates from OTP and is generated and programmed by OEM.

**Figure 1** Secure Boot Mode Decryption Relationship Diagram<a name="fig1739414716164"></a>
![](figures/安全启动模式解密关系图.png "安全启动模式解密关系图")

# Boot Image Creation and Programming
SS928V100 supports multiple boot schemes. The creation and programming steps for boot images must correspond to the boot scheme. Additionally, the OTP of SS928V100 controls the boot flow, including boot scheme selection, image legitimacy verification, and version verification, and must be configured and programmed according to the boot scheme.

This chapter describes the SS928V100 image creation steps, OTP programming steps, image programming methods, and provides reference values for environment variable configuration.

Before starting, the following must be clarified:

-   Which boot scheme is to be used? For an introduction to boot schemes, please refer to "[Boot Schemes](#ZH-CN_TOPIC_0000002424357774)";
-   Whether dual-signature (Third\_party signing of the image) functionality is required. For related information, please refer to "[SoC Secure Boot Public Key Framework](#ZH-CN_TOPIC_0000002424197942)".

## Boot Image Creation Steps<a name="ZH-CN_TOPIC_0000002424197890"></a>

The image creation method for the fast boot scheme is the same as the traditional boot scheme. To create boot images for non-secure boot and secure boot, the "image\_map" image creation script needs to be used. This section describes the image creation steps for each boot scheme of SS928V100.

### Fast Boot<a name="ZH-CN_TOPIC_0000002424197934"></a>

When using the fast boot scheme, the following images need to be created:

-   U-Boot image
-   ATF+Kernel image
-   Filesystem image

For image compilation and creation methods, please refer to "osdrv/readme\_cn.txt".

### Non-Secure Boot<a name="ZH-CN_TOPIC_0000002457836493"></a>

When using the non-secure boot scheme, the following images need to be created:

-   ATF+Kernel image
-   Filesystem image
-   Boot image

Image characteristics and creation instructions are as follows:

-   The compilation and creation methods for the ATF+Kernel image and filesystem image can be found in "osdrv/readme\_cn.txt".
-   The Boot image contains the binary code of GSL and U-Boot and needs to be created using the "image\_map" image creation script.

The following are the specific steps for creating the Boot image:

1.  Enter the `osdrv/components/` directory, extract `boot.tar.gz`, and obtain the GSL code and "image\_map" image creation script.

    ```
    tar xf boot.tar.gz
    ```

    The GSL source code and "image\_map" image creation script are located in the `boot/gsl/` directory and `boot/image_map/` directory, respectively.

2.  Compile GSL to obtain the GSL image `gsl.bin`.

    ```
    cd boot/gsl/
    make CHIP=ss928v100
    ```

    The GSL binary image `gsl.bin` will be generated in the `pub/` directory.

3.  Enter the `open_source/u-boot/` directory and compile U-Boot to obtain the U-Boot image `u-boot-ss928v100.bin`.

    For compilation methods, please refer to "osdrv/readme\_cn.txt".

4.  Copy the compiled GSL and U-Boot images, along with the U-Boot table, to the `image_map/` directory.

    ```
    cp osdrv/components/boot/gsl/pub/gsl.bin osdrv/components/boot/image_map/
    cp open_source/u-boot/u-boot-2020.01/u-boot-ss928v100.bin osdrv/components/boot/image_map/u-boot-original.bin
    cp open_source/u-boot/u-boot-2020.01/.reg osdrv/components/boot/image_map/.reg
    ```

5.  Enter the `osdrv/components/boot/image_map/` directory and create the non-secure boot Boot image.

    ```
    cd osdrv/components/boot/image_map/
    python oem/oem_quick_build.py
    ```

    The binary file `boot_image.bin` generated in the `image/oem/` directory is the non-secure boot Boot image.

### Secure Boot<a name="ZH-CN_TOPIC_0000002457876637"></a>

When using the secure boot scheme, the following images need to be created:

-   ATF+Kernel image
-   Filesystem image
-   Boot image

Image characteristics and creation instructions are as follows:

-   The ATF+Kernel image and filesystem image used for secure boot are the same as for non-secure boot. Compilation and creation methods can be found in "osdrv/readme\_cn.txt".
-   The secure boot Boot image not only includes the GSL image and U-Boot image, but also data used to ensure the integrity, legitimacy, and confidentiality of the Boot image, including asymmetric keys, symmetric keys, MSID, and version numbers. These data are managed by the Owner of each region.
-   When creating the Boot image, each Owner passes data to the image creation script through a JSON configuration file.
-   Different boot scenarios (e.g., whether GSL and U-Boot need encryption) depend on different configuration items, and the required configuration files may vary. For ease of use, the image creation script also provides functionality to generate configuration files based on the boot scenario.

The following are the steps for OEM to create the Boot image:

1.  Compile GSL to obtain the GSL image `gsl.bin`.

    The operation is the same as steps 1-2 in "[Non-Secure Boot](#ZH-CN_TOPIC_0000002457836493)".

2.  Compile U-Boot to obtain the U-Boot image `u-boot-ss928v100.bin`.

    The operation is the same as step 3 in "[Non-Secure Boot](#ZH-CN_TOPIC_0000002457836493)".

3.  Enter the `osdrv/components/boot/image_map/` directory and generate the OEM JSON configuration file `oem_config.json`.

    ```
    cd osdrv/components/boot/image_map/
    python oem/oem_main.py gencfg oem/oem_config.json
    ```

    The option selection method is as follows:

    ```
    Security Mode:
    0.Non-Secure
    1.Secure
    > 1
    Input:1
    Start Flow:
    0.Non-TEE
    1.TEE
    > 0
    Input:0
    Encrypt GSL Code:
    0.No
    1.YES
    > (Enter 0 for GSL not encrypted, 1 for GSL encrypted)
    Encrypt Boot Code:
    0.No
    1.YES
    > (Enter 0 for U-Boot not encrypted, 1 for U-Boot encrypted)
    ```

    After completing the option selection, the configuration file `oem/oem_config.json` will be generated.

4.  Fill in the unconfigured fields in `oem_config.json` (enclosed by "/* */", remove "/* */" when filling). For configuration methods, please refer to the "SS928V100/SS927V100 Secure Boot Script Configuration Guide" document. For the `GSL_Code` and `Boot_Code` fields, fill in the paths to `gsl.bin` and `u-boot-ss928v100.bin` generated in steps 1 and 2 respectively. For the `Cfg_Param` field, fill in the path to the U-Boot table (the `.reg` file used for compiling U-Boot in step 2).

5.  Create a Boot image with OEM signature.

    ```
    python oem/oem_main.py build oem/oem_config.json
    ```

    The `boot_image.bin` in the `image/oem/` directory is the secure boot Boot image.

If a Third\_party needs to sign the Boot image, the following operations must be completed:

1.  Enter the `osdrv/components/boot/image_map/` directory and confirm that the OEM-generated single-signature Boot image is in the `image/oem/` directory, named `boot_image.bin`.
2.  Generate the Third party JSON configuration file `third_party_config.json`.

    ```
    python third_party/third_party_main.py gencfg third_party/third_party_config.json
    Start Flow:
    0.Non-TEE
    1.TEE
    > 0
    Input:0
    ```

    After completing the option selection, the configuration file `third_party/third_party_config.json` will be generated.

3.  Fill in the unconfigured fields in `third_party_config.json` (enclosed by "/* */", remove "/* */" when filling). For configuration methods, please refer to the "SS928V100/SS927V100 Secure Boot Script Configuration Guide" document.
4.  Sign the Boot image.

    ```
    python third_party/third_party_main.py build third_party/third_party_config.json
    ```

    The `boot_image.bin` in the `image/third_party/` directory is the dual-signature (signed by both OEM and Third\_party) secure boot Boot image.

## OTP Configuration and Programming<a name="ZH-CN_TOPIC_0000002457876665"></a>

SS928V100 supports multiple boot schemes. The boot scheme used by the chip needs to be configured through OTP. This section describes the OTP configuration method and how to use U-Boot to complete OTP programming.

Please be aware of the following before reading:

-   OTP programming operations cannot be undone. Incorrect OTP configuration and programming may cause irreparable boot failures or even introduce security risks. Please proceed with caution.
-   The "osdrv/components/boot.tar.gz" package provides an OTP programming code example at "image\_map/sample/write\_otp\_fun.c". This section uses this example to complete OTP configuration and programming.
-   The operations described in this section will generate a Boot image used for programming OTP. Please distinguish this Boot image from the one generated in "[Boot Image Creation Steps](#ZH-CN_TOPIC_0000002424197890)".

The following are the specific steps for OTP configuration and programming:

1.  Enter the `osdrv/components/` directory and create a directory `boot-otp` for creating the Boot image.

    ```
    cd osdrv/components/
    mkdir boot-otp/
    tar xf boot.tar.gz --strip-components=1 -C boot-otp/
    ```

2.  Enter the `open_source/u-boot/` directory, create a directory `u-boot-otp` for compiling U-Boot, and copy `osdrv/components/boot-otp/image_map/sample/write_otp_fun.c` to the `open_source/u-boot/u-boot-otp/cmd/` directory.

    ```
    cd open_source/u-boot/
    mkdir u-boot-otp/
    tar xf u-boot-2020.01.tar.bz2 --strip-components=1 -C u-boot-otp/
    cd u-boot-otp/
    patch -p1 < ../u-boot-2020.01.patch
    cp ../../../osdrv/components/boot-otp/image_map/sample/write_otp_fun.c ./cmd/
    ```

3.  Configure the OTP fields to be programmed in the `g_otp_startup_burn_fields` array in the `./cmd/write_otp_fun.c` file. [Table 1](#_table192164754414) specifies the OTP fields that need to be configured for different boot schemes, along with configuration references. "√" indicates the field needs to be configured; "-" indicates the field configuration is invalid. Please refer to the "Security Subsystem Usage Guide" to determine the values of each OTP field, then uncomment the OTP fields as needed in the `g_otp_startup_burn_fields` array and fill in the field values (hexadecimal strings starting with "0x").

    **Table 1** OTP Fields Required for Each Boot Scheme

    <a name="_table192164754414"></a>
    <table><thead align="left"><tr id="row501mcpsimp"><th class="cellrowborder" valign="top" width="18.85%" id="mcps1.2.6.1.1"><p id="p503mcpsimp"><a name="p503mcpsimp"></a><a name="p503mcpsimp"></a>Field<strong id="b4441162975213"><a name="b4441162975213"></a><a name="b4441162975213"></a>Name</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="9.49%" id="mcps1.2.6.1.2"><p id="p505mcpsimp"><a name="p505mcpsimp"></a><a name="p505mcpsimp"></a>Fast Boot</p>
    </th>
    <th class="cellrowborder" valign="top" width="12.559999999999999%" id="mcps1.2.6.1.3"><p id="p507mcpsimp"><a name="p507mcpsimp"></a><a name="p507mcpsimp"></a>Non-Secure Boot</p>
    </th>
    <th class="cellrowborder" valign="top" width="17.69%" id="mcps1.2.6.1.4"><p id="p509mcpsimp"><a name="p509mcpsimp"></a><a name="p509mcpsimp"></a>Secure Boot</p>
    </th>
    <th class="cellrowborder" valign="top" width="41.410000000000004%" id="mcps1.2.6.1.5"><p id="p513mcpsimp"><a name="p513mcpsimp"></a><a name="p513mcpsimp"></a>Reference Values and Notes</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row515mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p517mcpsimp"><a name="p517mcpsimp"></a><a name="p517mcpsimp"></a>quick_boot</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="p519mcpsimp"><a name="p519mcpsimp"></a><a name="p519mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="p521mcpsimp"><a name="p521mcpsimp"></a><a name="p521mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p523mcpsimp"><a name="p523mcpsimp"></a><a name="p523mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p527mcpsimp"><a name="p527mcpsimp"></a><a name="p527mcpsimp"></a>0x5: Fast boot;</p>
    <p id="p528mcpsimp"><a name="p528mcpsimp"></a><a name="p528mcpsimp"></a>0xF: Non-secure boot and secure boot.</p>
    </td>
    </tr>
    <tr id="row529mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p531mcpsimp"><a name="p531mcpsimp"></a><a name="p531mcpsimp"></a>secure_boot_en</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry532mcpsimpp0"><a name="entry532mcpsimpp0"></a><a name="entry532mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="p534mcpsimp"><a name="p534mcpsimp"></a><a name="p534mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p536mcpsimp"><a name="p536mcpsimp"></a><a name="p536mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p540mcpsimp"><a name="p540mcpsimp"></a><a name="p540mcpsimp"></a>0x42: Non-secure boot;</p>
    <p id="p541mcpsimp"><a name="p541mcpsimp"></a><a name="p541mcpsimp"></a>0xFF: Secure boot.</p>
    <p id="p542mcpsimp"><a name="p542mcpsimp"></a><a name="p542mcpsimp"></a>Before enabling secure boot, the SCS_simulate_flag in the image can be used to simulate the behavior of secure_boot_en being enabled for debugging the <a href="#ZH-CN_TOPIC_0000002457876645">Boot Flash Mapping</a> area, preventing irreparable chip errors due to incorrect OTP programming. Please refer to the description of the SCS_simulate_flag in the "SS928V100/SS927V100 Secure Boot Script Configuration Guide".</p>
    </td>
    </tr>
    <tr id="row556mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p558mcpsimp"><a name="p558mcpsimp"></a><a name="p558mcpsimp"></a>gsl_dec_en</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry559mcpsimpp0"><a name="entry559mcpsimpp0"></a><a name="entry559mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="p561mcpsimp"><a name="p561mcpsimp"></a><a name="p561mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p563mcpsimp"><a name="p563mcpsimp"></a><a name="p563mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p567mcpsimp"><a name="p567mcpsimp"></a><a name="p567mcpsimp"></a>0xF: GSL decryption enabled;</p>
    <p id="p568mcpsimp"><a name="p568mcpsimp"></a><a name="p568mcpsimp"></a>0xA: Whether to decrypt GSL depends on the GSL_Code_Enc_Flag in the image.</p>
    <p id="p569mcpsimp"><a name="p569mcpsimp"></a><a name="p569mcpsimp"></a>The "SS928V100/SS927V100 Secure Boot Script Configuration Guide" describes the GSL_Code_Enc_Flag configuration method. GSL is not decrypted only when gsl_dec_en is configured as 0xA and GSL_Code_Enc_Flag is configured as 0x3C7896E1.</p>
    </td>
    </tr>
    <tr id="row570mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p572mcpsimp"><a name="p572mcpsimp"></a><a name="p572mcpsimp"></a>bload_dec_en</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry573mcpsimpp0"><a name="entry573mcpsimpp0"></a><a name="entry573mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="p575mcpsimp"><a name="p575mcpsimp"></a><a name="p575mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p577mcpsimp"><a name="p577mcpsimp"></a><a name="p577mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p581mcpsimp"><a name="p581mcpsimp"></a><a name="p581mcpsimp"></a>0x1: U-Boot decryption enabled;</p>
    <p id="p582mcpsimp"><a name="p582mcpsimp"></a><a name="p582mcpsimp"></a>0x0: Whether to decrypt U-Boot depends on the Boot_Enc_Flag in the image.</p>
    <p id="p583mcpsimp"><a name="p583mcpsimp"></a><a name="p583mcpsimp"></a>The "SS928V100/SS927V100 Secure Boot Script Configuration Guide" describes the Boot_Enc_Flag configuration method. U-Boot is not decrypted only when bload_dec_en is configured as 0x0 and Boot_Enc_Flag is configured as 0x3C7896E1.</p>
    </td>
    </tr>
    <tr id="row597mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p599mcpsimp"><a name="p599mcpsimp"></a><a name="p599mcpsimp"></a>uboot_redundance</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry600mcpsimpp0"><a name="entry600mcpsimpp0"></a><a name="entry600mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry601mcpsimpp0"><a name="entry601mcpsimpp0"></a><a name="entry601mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p603mcpsimp"><a name="p603mcpsimp"></a><a name="p603mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p607mcpsimp"><a name="p607mcpsimp"></a><a name="p607mcpsimp"></a>0x0: Disable Boot Image backup.</p>
    <p id="p608mcpsimp"><a name="p608mcpsimp"></a><a name="p608mcpsimp"></a>0x1: Enable Boot Image backup;</p>
    </td>
    </tr>
    <tr id="row611mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p613mcpsimp"><a name="p613mcpsimp"></a><a name="p613mcpsimp"></a>oem_rk_deob_en</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry614mcpsimpp0"><a name="entry614mcpsimpp0"></a><a name="entry614mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry615mcpsimpp0"><a name="entry615mcpsimpp0"></a><a name="entry615mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p617mcpsimp"><a name="p617mcpsimp"></a><a name="p617mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p621mcpsimp"><a name="p621mcpsimp"></a><a name="p621mcpsimp"></a>The field value must be consistent with the oem_rk_deob_en value used by the KDFTool in the "SS928V100/SS927V100 Secure Boot Script Configuration Guide". If inconsistent, secure boot will fail.</p>
    </td>
    </tr>
    <tr id="row622mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p624mcpsimp"><a name="p624mcpsimp"></a><a name="p624mcpsimp"></a>oem_root_public_key_sha256</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry625mcpsimpp0"><a name="entry625mcpsimpp0"></a><a name="entry625mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry626mcpsimpp0"><a name="entry626mcpsimpp0"></a><a name="entry626mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p628mcpsimp"><a name="p628mcpsimp"></a><a name="p628mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p632mcpsimp"><a name="p632mcpsimp"></a><a name="p632mcpsimp"></a>Fill in the SHA256 checksum of the OEM_Root_Public_Key Area (see "OEM_Root_Public_Key Area" for related principles). After OEM creates the Boot image, this value can be obtained from the file "osdrv/components/boot/image_map/oem/tmp/oem_root_public_key_area_checksum.txt".</p>
    </td>
    </tr>
    <tr id="row633mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p635mcpsimp"><a name="p635mcpsimp"></a><a name="p635mcpsimp"></a>oem_root_symc_key0</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry636mcpsimpp0"><a name="entry636mcpsimpp0"></a><a name="entry636mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry637mcpsimpp0"><a name="entry637mcpsimpp0"></a><a name="entry637mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p639mcpsimp"><a name="p639mcpsimp"></a><a name="p639mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>This field is the OTP KEY described in "<a href="#ZH-CN_TOPIC_0000002457836485">Chip Key Derivation</a>". It is <strong id="b646mcpsimp"><a name="b646mcpsimp"></a><a name="b646mcpsimp"></a>sensitive information and must not be disclosed</strong>. The field value must be consistent with the oem_root_symc_key field used by the KDFTool in the "SS928V100/SS927V100 Secure Boot Script Configuration Guide", and cannot be all zeros; otherwise, secure boot will fail.</p>
    </td>
    </tr>
    <tr id="row647mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p649mcpsimp"><a name="p649mcpsimp"></a><a name="p649mcpsimp"></a>oem_root_symc_key0_flag</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry650mcpsimpp0"><a name="entry650mcpsimpp0"></a><a name="entry650mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry651mcpsimpp0"><a name="entry651mcpsimpp0"></a><a name="entry651mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p653mcpsimp"><a name="p653mcpsimp"></a><a name="p653mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p657mcpsimp"><a name="p657mcpsimp"></a><a name="p657mcpsimp"></a>Control flag for oem_root_symc_key0; fill in 0x00000000.</p>
    </td>
    </tr>
    <tr id="row658mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p660mcpsimp"><a name="p660mcpsimp"></a><a name="p660mcpsimp"></a>oem_msid</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry661mcpsimpp0"><a name="entry661mcpsimpp0"></a><a name="entry661mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry662mcpsimpp0"><a name="entry662mcpsimpp0"></a><a name="entry662mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p664mcpsimp"><a name="p664mcpsimp"></a><a name="p664mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p668mcpsimp"><a name="p668mcpsimp"></a><a name="p668mcpsimp"></a>OEM customer market segment identifier (ID). If it does not match the OEM_MSID_Ext in the "SS928V100/SS927V100 Secure Boot Script Configuration Guide", secure boot will fail.</p>
    </td>
    </tr>
    <tr id="row669mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p671mcpsimp"><a name="p671mcpsimp"></a><a name="p671mcpsimp"></a>oem_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry672mcpsimpp0"><a name="entry672mcpsimpp0"></a><a name="entry672mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry673mcpsimpp0"><a name="entry673mcpsimpp0"></a><a name="entry673mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p675mcpsimp"><a name="p675mcpsimp"></a><a name="p675mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p679mcpsimp"><a name="p679mcpsimp"></a><a name="p679mcpsimp"></a>OEM version number. The number of Bit 1s in the field represents the version number, used for Boot Image anti-rollback. If the version number indicated by OEM_Version_Ext in the "SS928V100/SS927V100 Secure Boot Script Configuration Guide" is less than the version number indicated by this field, secure boot will fail.</p>
    </td>
    </tr>
    <tr id="row700mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p702mcpsimp"><a name="p702mcpsimp"></a><a name="p702mcpsimp"></a>double_sign_en</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry703mcpsimpp0"><a name="entry703mcpsimpp0"></a><a name="entry703mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="p705mcpsimp"><a name="p705mcpsimp"></a><a name="p705mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p707mcpsimp"><a name="p707mcpsimp"></a><a name="p707mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p711mcpsimp"><a name="p711mcpsimp"></a><a name="p711mcpsimp"></a>0xA: Disable dual signature;</p>
    <p id="p712mcpsimp"><a name="p712mcpsimp"></a><a name="p712mcpsimp"></a>0xF: Enable dual signature.</p>
    <p id="p713mcpsimp"><a name="p713mcpsimp"></a><a name="p713mcpsimp"></a>After enabling dual signature, Third_party must sign the boot image. The dual signature operation by Third_party is described in "<a href="#ZH-CN_TOPIC_0000002424357722">Secure Boot</a>".</p>
    </td>
    </tr>
    <tr id="row718mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p720mcpsimp"><a name="p720mcpsimp"></a><a name="p720mcpsimp"></a>tp_root_public_key_sha256</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry721mcpsimpp0"><a name="entry721mcpsimpp0"></a><a name="entry721mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry722mcpsimpp0"><a name="entry722mcpsimpp0"></a><a name="entry722mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p724mcpsimp"><a name="p724mcpsimp"></a><a name="p724mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p728mcpsimp"><a name="p728mcpsimp"></a><a name="p728mcpsimp"></a>This field is related to dual signature and is only valid when double_sign_en is enabled. Fill in the SHA256 checksum of the Third_party_Root_Public_Key Area (see "<a href="#ZH-CN_TOPIC_0000002457876617">Third_party_Root_Public_Key Area</a>" for related principles). After Third_party performs dual signature on the Boot image, this value can be obtained from the file "osdrv/components/boot/image_map/third_party/tmp/third_party_root_public_key_area_checksum.txt".</p>
    </td>
    </tr>
    <tr id="row731mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p733mcpsimp"><a name="p733mcpsimp"></a><a name="p733mcpsimp"></a>third_party_msid</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry734mcpsimpp0"><a name="entry734mcpsimpp0"></a><a name="entry734mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry735mcpsimpp0"><a name="entry735mcpsimpp0"></a><a name="entry735mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p737mcpsimp"><a name="p737mcpsimp"></a><a name="p737mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p741mcpsimp"><a name="p741mcpsimp"></a><a name="p741mcpsimp"></a>This field is related to dual signature and is only valid when double_sign_en is enabled. It represents the third-party market segment identifier (ID). If it does not match the Third_party_MSID_Ext in the "SS928V100/SS927V100 Secure Boot Script Configuration Guide", secure boot will fail.</p>
    </td>
    </tr>
    <tr id="row742mcpsimp"><td class="cellrowborder" valign="top" width="18.85%" headers="mcps1.2.6.1.1 "><p id="p744mcpsimp"><a name="p744mcpsimp"></a><a name="p744mcpsimp"></a>third_party_version</p>
    </td>
    <td class="cellrowborder" valign="top" width="9.49%" headers="mcps1.2.6.1.2 "><p id="entry745mcpsimpp0"><a name="entry745mcpsimpp0"></a><a name="entry745mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="12.559999999999999%" headers="mcps1.2.6.1.3 "><p id="entry746mcpsimpp0"><a name="entry746mcpsimpp0"></a><a name="entry746mcpsimpp0"></a>-</p>
    </td>
    <td class="cellrowborder" valign="top" width="17.69%" headers="mcps1.2.6.1.4 "><p id="p748mcpsimp"><a name="p748mcpsimp"></a><a name="p748mcpsimp"></a>√</p>
    </td>
    <td class="cellrowborder" valign="top" width="41.410000000000004%" headers="mcps1.2.6.1.5 "><p id="p752mcpsimp"><a name="p752mcpsimp"></a><a name="p752mcpsimp"></a>This field is related to dual signature and is only valid when double_sign_en is enabled. The number of Bit 1s in the field represents the third-party version number, used for Boot Image anti-rollback. If the version number indicated by Third_party_Version_Ext in the "SS928V100/SS927V100 Secure Boot Script Configuration Guide" is less than the version number indicated by this field, secure boot will fail.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Add the following content to the `./cmd/Makefile` file to include the OTP programming command compilation item.

    ```
    obj-y += write_otp_fun.o
    ```

5.  Add the following macro definition in the `./include/configs/ss928v100.h` file to enable the OTP driver.

    ```
    #define CONFIG_OTP_ENABLE
    ```

6.  Compile U-Boot with the OTP programming command.

    Before compiling U-Boot, use a Windows system to enter the `osdrv/tools/pc/uboot_tools/` directory, open the Excel file for the corresponding board, select the `main` tab, and click the "Generate reg bin file" button to generate the U-Boot table file `reg_info.bin` for the corresponding platform. Then return to the Linux system to execute the operations:

    ```
    cp configs/ss928v100_defconfig .config
    make ARCH=arm CROSS_COMPILE=aarch64-v01c01-linux-gnu- menuconfig
    make ARCH=arm CROSS_COMPILE=aarch64-v01c01-linux-gnu- -j 20
    cp ../../../osdrv/tools/pc/uboot_tools/reg_info.bin .reg
    make ARCH=arm CROSS_COMPILE=aarch64-v01c01-linux-gnu- u-boot-z.bin
    ```

    The above operations take SPI NOR/NAND as the boot medium as an example. If the boot medium is eMMC, change the configuration file `configs/ss928v100_defconfig` to `ss928v100_emmc_defconfig`.

7.  Verify OTP configuration values (optional step).

    Enter the `osdrv/components/boot-otp/image_map/` directory, open `oem/otp_check.json`, fill in the OTP values set in "Step 3", and then execute the command:

    ```
    # Obtain the KDF tool
    cp ../../../tools/pc/kdf_customer/parameter.bin ./
    tar xf ../../../tools/pc/kdf_customer/KDFTools_V1.0.3.tar.gz --strip-components=1
    # Verify OTP configuration values (choose one of the following commands based on the boot scenario)
    # Secure boot
    python3 oem/oem_main.py check oem/otp_check.json <Boot Image Path>
    ```

    Replace "<Boot Image Path\>" in the command with the actual image path generated in "[Boot Image Creation Steps](#ZH-CN_TOPIC_0000002424197890)".

    Printing "Boot Image is OK." indicates that the OTP configuration values of the Boot Image have passed verification; an error indicates incorrect OTP configuration values.

8.  Enter the `osdrv/components/boot-otp/gsl/` directory and compile the GSL image to obtain `gsl.bin`.

    ```
    make CHIP=ss928v100
    ```

9.  Enter `osdrv/components/boot-otp/image_map` to create the Boot image.

    ```
    cp ../../../../open_source/u-boot/u-boot-otp/u-boot-ss928v100.bin ./u-boot-original.bin
    cp ../../../../open_source/u-boot/u-boot-otp/.reg ./
    cp ../gsl/pub/gsl.bin ./
    python oem/oem_quick_build.py
    ```

    The `boot_image.bin` generated in the `image/oem/` directory has OTP programming capability.

10. Program the new `image/oem/boot_image.bin` to the storage medium.
11. After programming is complete, reset and enter U-Boot, then execute the `write_otp` command to complete OTP programming.

This completes the OTP programming. Afterwards, follow the description in "[Image Programming](#ZH-CN_TOPIC_0000002457836489)" to program the boot image created in "[Boot Image Creation Steps](#ZH-CN_TOPIC_0000002424197890)", and configure the environment variables in U-Boot according to "[Board Environment Variable Configuration Reference](#ZH-CN_TOPIC_0000002424357730)". After configuring the environment variables, reset the chip to verify whether the system boots successfully.

>![](public_sys-resources/icon-notice.gif) **Caution:**
>-   The keys programmed into OTP are sensitive information and must be kept confidential. This example code is only for programming OTP. For formal release, the `write_otp_fun.c` file used for OTP programming must be deleted from U-Boot; otherwise, there is a risk of key leakage.
>-   It is strongly recommended that customers set all feature/function switch bits to their required values and force lock them before final product release. Even if default values meet requirements, locking is still required.
>-   After programming OTP, the OTP values take effect only after the chip is powered off and on again, or by using the `dog_reset` command in U-Boot. Chip soft reset will not take effect.
>-   The SCS\_simulate\_flag in the Unchecked Area for Vendor within the image structure can be used for secure boot debugging when secure boot is not enabled.

## Image Programming<a name="ZH-CN_TOPIC_0000002457836489"></a>

This section uses the SPI NOR storage medium as an example to describe how to use the ToolPlatform tool to program the boot image.

When using other storage media (SPI NAND, eMMC), the filesystem type and programming length differ from SPI NOR, but the remaining image sizes and programming layout are the same as SPI NOR.

### Fast Boot<a name="ZH-CN_TOPIC_0000002424197910"></a>

The image programming layout for fast boot is shown in [Figure 1](#_fig1991144012019).

**Figure 1** Fast Boot ToolPlatform Programming Partition Reference Diagram<a name="_fig1991144012019"></a>
![](figures/快速启动ToolPlatform烧写分区参考图.png "快速启动ToolPlatform烧写分区参考图")

### Non-Secure Boot and Non-TEE Secure Boot<a name="ZH-CN_TOPIC_0000002457836497"></a>

The image programming layout is shown in [Figure 1](#__Ref55287952).

**Figure 1** ToolPlatform Programming Partition Reference Diagram<a name="__Ref55287952"></a>
![](figures/ToolPlatform烧写分区参考图.png "ToolPlatform烧写分区参考图")

>![](public_sys-resources/icon-notice.gif) **Caution:**
>The `uImage_ss928v100` file programmed in [Figure 1](#_fig1991144012019) and [Figure 1](#__Ref55287952) is the ATF+Kernel image.

## Board Environment Variable Configuration Reference<a name="ZH-CN_TOPIC_0000002424357730"></a>

This section provides examples of environment variable configuration when using SPI NOR, SPI NAND, and eMMC as the boot medium, based on the image layout from "[Image Programming](#ZH-CN_TOPIC_0000002457836489)".

-   SPI NOR

    ```
    setenv bootargs 'mem=128M console=ttyAMA0,115200 root=/dev/mtdblock2 rw rootfstype=jffs2 mtdparts=sfc:1M(boot),12M(kernel),18M(rootfs)';sa  setenv bootcmd 'sf probe 0;sf read 0x42000000 0x100000 0xc00000;bootm 0x42000000';sa
    ```

-   SPI NAND and Parallel NAND

    ```
    setenv bootargs 'mem=128M console=ttyAMA0,115200 clk_ignore_unused ubi.mtd=2 root=ubi0:ubifs rootfstype=ubifs rw mtdparts=nand:1M(boot),12M(kernel),32M(rootfs.ubifs)';sa   setenv bootcmd 'nand read 0x42000000 0x100000 0xc00000;bootm 0x42000000';sa
    ```

-   eMMC

    ```
    setenv bootargs 'mem=128M console=ttyAMA0,115200 clk_ignore_unused rw rootwait root=/dev/mmcblk0p3 rootfstype=ext4 blkdevparts=mmcblk0:1M(boot),12M(kernel),96M(rootfs)';sa  setenv bootcmd 'mmc read 0 0x42000000 0x800 0x6000; bootm 0x42000000';sa
    ```

# Secure Boot Image Backup Feature
To use the secure Boot image backup feature, first program the "uboot\_redundance" field in OTP (see the "OTP Configuration and Programming" section for details).

The programmed backup Boot Image start address must be 64K-aligned and within the first 1MB of the storage medium. When the primary Boot Image verification fails, the boot program searches for an available backup Boot Image on the boot medium and boots from it.

>![](public_sys-resources/icon-caution.gif) **Note:**
>When the storage medium is NAND Flash, do not erase the first block of the medium; otherwise, there is a risk of backup failure.

# Reference for Kernel and Filesystem Secure Boot Signature Verification Solution
This reference solution is based on the features of the above secure boot solution. After U-Boot passes signature verification, it implements kernel signature verification in U-Boot. Before the previous stage boots the next stage system, it performs signature verification on the system to be booted. If verification succeeds, the Linux system is booted; otherwise, the system fails to boot. The signature verification mechanism ensures the integrity of the system image. If the image is tampered with or damaged, the system will not boot.

## Secure Boot Flow<a name="ZH-CN_TOPIC_0000002457876633"></a>

The description in this document only covers BOOTROM verification before booting U-Boot, and U-Boot verification before booting the Kernel, as shown in [Figure 1](#fig135231753812). The verification flow for other components such as the filesystem, as well as related data encryption/decryption protection, can be designed and developed following this model and is not described in this document.

The solution first aligns the size of the non-secure U-Boot original image to 16 bytes before the image, then appends information such as the kernel's secure verification public key to the end of the Boot original image. After appending this information, a new secure boot image is generated through "[Boot Image Creation Steps](#ZH-CN_TOPIC_0000002424197890)".

**Figure 1** Kernel and Filesystem Boot Verification Flow Block Diagram<a name="fig135231753812"></a>
![](figures/内核及文件系统启动验签流程框图.png "内核及文件系统启动验签流程框图")

For the hash calculation and asymmetric RSA encryption/decryption involved in the secure boot verification flow, please consult relevant resources on your own; this document does not elaborate further. For further development of encryption/decryption functionality, you may explore other encryption algorithms, such as the symmetric AES encryption algorithm.

## U-Boot Image Structure with Verification Information<a name="ZH-CN_TOPIC_0000002424357746"></a>

The structure of the U-Boot image with appended verification information is shown in [Figure 1](#fig13141855185214). Kernel-related security information is appended to the end of the U-Boot image, and then the U-Boot image with Kernel verification information is made into a secure boot image.

**Figure 1** U-Boot Image Structure with Verification Information<a name="fig13141855185214"></a>
![](figures/附验证信息U-Boot镜像结构.png "附验证信息U-Boot镜像结构")

## Secure Kernel Image Structure<a name="ZH-CN_TOPIC_0000002457836509"></a>

The secure Kernel image consists of header information, the Kernel image, and signature information, as shown in [Figure 1](#fig47919505579). It is assembled on top of the original Kernel image structure, where the Kernel image is a compressed image. The RSA public key used for Kernel signature verification is stored in the U-Boot original image and is integrated into the secure boot image along with the secure image.

**Figure 1** Secure Kernel Image Structure Diagram<a name="fig47919505579"></a>
![](figures/安全Kernel镜像结构图.png "安全Kernel镜像结构图")

## Functional Implementation<a name="ZH-CN_TOPIC_0000002424197894"></a>

For implementing the U-Boot signature verification of the Kernel, please refer to the RSA signature and verification usage flow section in the "CIPHER API Reference" document, and call the corresponding API interfaces.

# Code Solution Reference for Increased U-Boot Table Size
>![](public_sys-resources/icon-caution.gif) **Note:**
>This method is only applicable to non-secure boot and secure boot and is invalid for fast boot.
>The modification must ensure that `gsl.bin` size (corresponding to GSL\_Code\_Area\_Len) + U-Boot table size (16-byte aligned) < 70.76KB.

## Purpose<a name="ZH-CN_TOPIC_0000002424357762"></a>

To increase the U-Boot table size limit from 10.77KB (0x2B10 bytes) to 16.00KB (0x4000 bytes).

## Method<a name="ZH-CN_TOPIC_0000002457836525"></a>

1.  Modify `gsl/include/flash_map.h`

    ```
    #define CFG_PARAM_SIZE 0x2B10
    ```

    Change to:

    ```
    #define CFG_PARAM_SIZE 0x4000
    ```

2.  Modify `image_map/common/area_tool.py`

    ```
    class AreaCfg:
    CFG_PARAM_SIZE = 0x2B10     # reg table size
    ```

    Change to:

    ```
    class AreaCfg:
    CFG_PARAM_SIZE = 0x4000     # reg table size.
    ```

# Error Code List
**Table 1** Error Code List

<a name="zh-cn_topic_0000001755879218_table17854135394813"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000001755879218_row17854165314482"><th class="cellrowborder" align="left" valign="top" width="12.45%" id="mcps1.2.3.1.1"><p id="zh-cn_topic_0000001755879218_p1485415318484"><a name="zh-cn_topic_0000001755879218_p1485415318484"></a><a name="zh-cn_topic_0000001755879218_p1485415318484"></a>Error Code</p>
</th>
<th class="cellrowborder" align="left" valign="top" width="87.55%" id="mcps1.2.3.1.2"><p id="zh-cn_topic_0000001755879218_p285410537485"><a name="zh-cn_topic_0000001755879218_p285410537485"></a><a name="zh-cn_topic_0000001755879218_p285410537485"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000001755879218_row17854145364815"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p17854135319489"><a name="zh-cn_topic_0000001755879218_p17854135319489"></a><a name="zh-cn_topic_0000001755879218_p17854135319489"></a>E4D1</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p3854115364817"><a name="zh-cn_topic_0000001755879218_p3854115364817"></a><a name="zh-cn_topic_0000001755879218_p3854115364817"></a>PCIe boot data acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row38543534487"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p15854753104815"><a name="zh-cn_topic_0000001755879218_p15854753104815"></a><a name="zh-cn_topic_0000001755879218_p15854753104815"></a>E4D2</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p11855185304820"><a name="zh-cn_topic_0000001755879218_p11855185304820"></a><a name="zh-cn_topic_0000001755879218_p11855185304820"></a>UART data download failed</p>
</td>
</tr>
<tr id="row144952937"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p3449122435"><a name="p3449122435"></a><a name="p3449122435"></a>E4D3</p>
</td>
<td class="cellrowborder" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p94494213312"><a name="p94494213312"></a><a name="p94494213312"></a>SD card data acquisition failed</p>
</td>
</tr>
<tr id="row1277314561218"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p177741956629"><a name="p177741956629"></a><a name="p177741956629"></a>E4D4</p>
</td>
<td class="cellrowborder" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p777485613219"><a name="p777485613219"></a><a name="p777485613219"></a>USB data download failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row1185511533481"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p1685545318488"><a name="zh-cn_topic_0000001755879218_p1685545318488"></a><a name="zh-cn_topic_0000001755879218_p1685545318488"></a>E4D5</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p1885565334817"><a name="zh-cn_topic_0000001755879218_p1885565334817"></a><a name="zh-cn_topic_0000001755879218_p1885565334817"></a>Flash backup acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row8855145344819"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p1985565310489"><a name="zh-cn_topic_0000001755879218_p1985565310489"></a><a name="zh-cn_topic_0000001755879218_p1985565310489"></a>E4D6</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p18855195311489"><a name="zh-cn_topic_0000001755879218_p18855195311489"></a><a name="zh-cn_topic_0000001755879218_p18855195311489"></a>Flash data acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row4855453104810"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p18551553104816"><a name="zh-cn_topic_0000001755879218_p18551553104816"></a><a name="zh-cn_topic_0000001755879218_p18551553104816"></a>E4D7</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p185545313480"><a name="zh-cn_topic_0000001755879218_p185545313480"></a><a name="zh-cn_topic_0000001755879218_p185545313480"></a>eMMC backup acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row185515530482"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p3855125394819"><a name="zh-cn_topic_0000001755879218_p3855125394819"></a><a name="zh-cn_topic_0000001755879218_p3855125394819"></a>E4D8</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p128552053174819"><a name="zh-cn_topic_0000001755879218_p128552053174819"></a><a name="zh-cn_topic_0000001755879218_p128552053174819"></a>eMMC data acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row11855153144818"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p1985535354815"><a name="zh-cn_topic_0000001755879218_p1985535354815"></a><a name="zh-cn_topic_0000001755879218_p1985535354815"></a>E6Dx</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p188551753174820"><a name="zh-cn_topic_0000001755879218_p188551753174820"></a><a name="zh-cn_topic_0000001755879218_p188551753174820"></a>GSL_Third_party_Key Area verification failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row2855253114812"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p168551753164819"><a name="zh-cn_topic_0000001755879218_p168551753164819"></a><a name="zh-cn_topic_0000001755879218_p168551753164819"></a>E7Dx</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p3855155310481"><a name="zh-cn_topic_0000001755879218_p3855155310481"></a><a name="zh-cn_topic_0000001755879218_p3855155310481"></a>GSL_Key_Area verification failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row785525304813"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p185515319481"><a name="zh-cn_topic_0000001755879218_p185515319481"></a><a name="zh-cn_topic_0000001755879218_p185515319481"></a>E8D1</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p11855115374812"><a name="zh-cn_topic_0000001755879218_p11855115374812"></a><a name="zh-cn_topic_0000001755879218_p11855115374812"></a>Flash GSL Code Area acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row885516539484"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p2085518532481"><a name="zh-cn_topic_0000001755879218_p2085518532481"></a><a name="zh-cn_topic_0000001755879218_p2085518532481"></a>E8D2</p>
</td>
<td class="cellrowborder" rowspan="2" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p385595394811"><a name="zh-cn_topic_0000001755879218_p385595394811"></a><a name="zh-cn_topic_0000001755879218_p385595394811"></a>eMMC GSL Code Area acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row128551653114812"><td class="cellrowborder" align="left" valign="top" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p1985515313481"><a name="zh-cn_topic_0000001755879218_p1985515313481"></a><a name="zh-cn_topic_0000001755879218_p1985515313481"></a>E8D3</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row585595318482"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p17855753144814"><a name="zh-cn_topic_0000001755879218_p17855753144814"></a><a name="zh-cn_topic_0000001755879218_p17855753144814"></a>E9Dx</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p485595324812"><a name="zh-cn_topic_0000001755879218_p485595324812"></a><a name="zh-cn_topic_0000001755879218_p485595324812"></a>GSL_Code_Area verification failed</p>
</td>
</tr>
<tr id="row18787107101918"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p87875711195"><a name="p87875711195"></a><a name="p87875711195"></a>G4S1</p>
</td>
<td class="cellrowborder" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p1122357192010"><a name="p1122357192010"></a><a name="p1122357192010"></a>PCIe boot data acquisition failed</p>
</td>
</tr>
<tr id="row14732102015191"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p492335018193"><a name="p492335018193"></a><a name="p492335018193"></a>G4S2</p>
</td>
<td class="cellrowborder" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p148641414202"><a name="p148641414202"></a><a name="p148641414202"></a>UART data download failed</p>
</td>
</tr>
<tr id="row47864132194"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p1824925131917"><a name="p1824925131917"></a><a name="p1824925131917"></a>G4S3</p>
</td>
<td class="cellrowborder" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p87861134191"><a name="p87861134191"></a><a name="p87861134191"></a>SD card data acquisition failed</p>
</td>
</tr>
<tr id="row7161181716198"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p084435110197"><a name="p084435110197"></a><a name="p084435110197"></a>G4S4</p>
</td>
<td class="cellrowborder" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p1262485012018"><a name="p1262485012018"></a><a name="p1262485012018"></a>USB data download failed</p>
</td>
</tr>
<tr id="row1464441021917"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p13348125271911"><a name="p13348125271911"></a><a name="p13348125271911"></a>G4S5</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p1964441091912"><a name="p1964441091912"></a><a name="p1964441091912"></a>Flash data acquisition failed</p>
</td>
</tr>
<tr id="row48610515192"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p169349529196"><a name="p169349529196"></a><a name="p169349529196"></a>G4S7</p>
</td>
</tr>
<tr id="row236852121910"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p12416145371912"><a name="p12416145371912"></a><a name="p12416145371912"></a>G4S6</p>
</td>
<td class="cellrowborder" rowspan="5" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p133681126199"><a name="p133681126199"></a><a name="p133681126199"></a>eMMC data acquisition failed</p>
</td>
</tr>
<tr id="row1740911412198"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p35461541199"><a name="p35461541199"></a><a name="p35461541199"></a>G4S8</p>
</td>
</tr>
<tr id="row70828182210"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p4949194482219"><a name="p4949194482219"></a><a name="p4949194482219"></a>G4S9</p>
</td>
</tr>
<tr id="row11179135102216"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p1236311479225"><a name="p1236311479225"></a><a name="p1236311479225"></a>G4Sa</p>
</td>
</tr>
<tr id="row18433120229"><td class="cellrowborder" valign="top" headers="mcps1.2.3.1.1 "><p id="p45261251122217"><a name="p45261251122217"></a><a name="p45261251122217"></a>G4Sb</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row15855135384818"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p18555533481"><a name="zh-cn_topic_0000001755879218_p18555533481"></a><a name="zh-cn_topic_0000001755879218_p18555533481"></a>G5Sx</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p128551153144816"><a name="zh-cn_topic_0000001755879218_p128551153144816"></a><a name="zh-cn_topic_0000001755879218_p128551153144816"></a>Boot Key Area verification failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row885535320489"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p785685311481"><a name="zh-cn_topic_0000001755879218_p785685311481"></a><a name="zh-cn_topic_0000001755879218_p785685311481"></a>G6Sx</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p19856105311483"><a name="zh-cn_topic_0000001755879218_p19856105311483"></a><a name="zh-cn_topic_0000001755879218_p19856105311483"></a>Boot Params Area verification failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row198562053144819"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p88561953134813"><a name="zh-cn_topic_0000001755879218_p88561953134813"></a><a name="zh-cn_topic_0000001755879218_p88561953134813"></a>G8s1</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p18856853114811"><a name="zh-cn_topic_0000001755879218_p18856853114811"></a><a name="zh-cn_topic_0000001755879218_p18856853114811"></a>PCIe boot data acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row208561553174813"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p98561953154810"><a name="zh-cn_topic_0000001755879218_p98561953154810"></a><a name="zh-cn_topic_0000001755879218_p98561953154810"></a>G8s2</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p185613530483"><a name="zh-cn_topic_0000001755879218_p185613530483"></a><a name="zh-cn_topic_0000001755879218_p185613530483"></a>UART data download failed</p>
</td>
</tr>
<tr id="row128584301436"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p985983015318"><a name="p985983015318"></a><a name="p985983015318"></a>G8s3</p>
</td>
<td class="cellrowborder" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p28596307315"><a name="p28596307315"></a><a name="p28596307315"></a>SD card data acquisition failed</p>
</td>
</tr>
<tr id="row582251039"><td class="cellrowborder" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="p88102512311"><a name="p88102512311"></a><a name="p88102512311"></a>G8s4</p>
</td>
<td class="cellrowborder" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="p18152518312"><a name="p18152518312"></a><a name="p18152518312"></a>USB data download failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row585613539487"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p88561953194814"><a name="zh-cn_topic_0000001755879218_p88561953194814"></a><a name="zh-cn_topic_0000001755879218_p88561953194814"></a>G8s5</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p108561953114814"><a name="zh-cn_topic_0000001755879218_p108561953114814"></a><a name="zh-cn_topic_0000001755879218_p108561953114814"></a>Flash data acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row16856253184812"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p1285605344819"><a name="zh-cn_topic_0000001755879218_p1285605344819"></a><a name="zh-cn_topic_0000001755879218_p1285605344819"></a>G8s6</p>
</td>
<td class="cellrowborder" rowspan="4" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p089241765415"><a name="zh-cn_topic_0000001755879218_p089241765415"></a><a name="zh-cn_topic_0000001755879218_p089241765415"></a>eMMC data acquisition failed</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row13856125314480"><td class="cellrowborder" align="left" valign="top" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p3856155316482"><a name="zh-cn_topic_0000001755879218_p3856155316482"></a><a name="zh-cn_topic_0000001755879218_p3856155316482"></a>G8s7</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row0856105313489"><td class="cellrowborder" align="left" valign="top" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p7856053184812"><a name="zh-cn_topic_0000001755879218_p7856053184812"></a><a name="zh-cn_topic_0000001755879218_p7856053184812"></a>G8s8</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row085617532482"><td class="cellrowborder" align="left" valign="top" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p108563536486"><a name="zh-cn_topic_0000001755879218_p108563536486"></a><a name="zh-cn_topic_0000001755879218_p108563536486"></a>G8s9</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001755879218_row285685384818"><td class="cellrowborder" align="left" valign="top" width="12.45%" headers="mcps1.2.3.1.1 "><p id="zh-cn_topic_0000001755879218_p108569533488"><a name="zh-cn_topic_0000001755879218_p108569533488"></a><a name="zh-cn_topic_0000001755879218_p108569533488"></a>G9Sx</p>
</td>
<td class="cellrowborder" align="left" valign="top" width="87.55%" headers="mcps1.2.3.1.2 "><p id="zh-cn_topic_0000001755879218_p2085685314486"><a name="zh-cn_topic_0000001755879218_p2085685314486"></a><a name="zh-cn_topic_0000001755879218_p2085685314486"></a>Boot Area verification failed</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **Note:**
>In the error code table, "x" represents any digit. For example, "G5Sx" refers to "G5S1", "G5S2", "G5S3", etc.

# Abbreviations
<a name="table345mcpsimp"></a>
<table><tbody><tr id="row350mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p352mcpsimp"><a name="p352mcpsimp"></a><a name="p352mcpsimp"></a><strong id="b353mcpsimp"><a name="b353mcpsimp"></a><a name="b353mcpsimp"></a>A</strong></p>
</td>
</tr>
<tr id="row354mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p356mcpsimp"><a name="p356mcpsimp"></a><a name="p356mcpsimp"></a>AES</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p358mcpsimp"><a name="p358mcpsimp"></a><a name="p358mcpsimp"></a>Advanced Encryption Standard</p>
</td>
</tr>
<tr id="row359mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p361mcpsimp"><a name="p361mcpsimp"></a><a name="p361mcpsimp"></a>ATF</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p363mcpsimp"><a name="p363mcpsimp"></a><a name="p363mcpsimp"></a>Arm Trust Firmware</p>
</td>
</tr>
<tr id="row364mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p366mcpsimp"><a name="p366mcpsimp"></a><a name="p366mcpsimp"></a><strong id="b367mcpsimp"><a name="b367mcpsimp"></a><a name="b367mcpsimp"></a>C</strong></p>
</td>
</tr>
<tr id="row368mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p370mcpsimp"><a name="p370mcpsimp"></a><a name="p370mcpsimp"></a>CPU</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p372mcpsimp"><a name="p372mcpsimp"></a><a name="p372mcpsimp"></a>Central Processing Unit</p>
</td>
</tr>
<tr id="row373mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p375mcpsimp"><a name="p375mcpsimp"></a><a name="p375mcpsimp"></a><strong id="b376mcpsimp"><a name="b376mcpsimp"></a><a name="b376mcpsimp"></a>G</strong></p>
</td>
</tr>
<tr id="row377mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p379mcpsimp"><a name="p379mcpsimp"></a><a name="p379mcpsimp"></a>GSL</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p381mcpsimp"><a name="p381mcpsimp"></a><a name="p381mcpsimp"></a>Secure Bootloader</p>
</td>
</tr>
<tr id="row382mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p384mcpsimp"><a name="p384mcpsimp"></a><a name="p384mcpsimp"></a><strong id="b385mcpsimp"><a name="b385mcpsimp"></a><a name="b385mcpsimp"></a>J</strong></p>
</td>
</tr>
<tr id="row386mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p388mcpsimp"><a name="p388mcpsimp"></a><a name="p388mcpsimp"></a>JTAG</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p390mcpsimp"><a name="p390mcpsimp"></a><a name="p390mcpsimp"></a>Joint Test Action Group</p>
</td>
</tr>
<tr id="row391mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p393mcpsimp"><a name="p393mcpsimp"></a><a name="p393mcpsimp"></a><strong id="b394mcpsimp"><a name="b394mcpsimp"></a><a name="b394mcpsimp"></a>K</strong></p>
</td>
</tr>
<tr id="row395mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p397mcpsimp"><a name="p397mcpsimp"></a><a name="p397mcpsimp"></a>KeyLadder</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p399mcpsimp"><a name="p399mcpsimp"></a><a name="p399mcpsimp"></a>A structured multi-level key mechanism that ensures secure transmission of control words.</p>
</td>
</tr>
<tr id="row400mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p402mcpsimp"><a name="p402mcpsimp"></a><a name="p402mcpsimp"></a><strong id="b403mcpsimp"><a name="b403mcpsimp"></a><a name="b403mcpsimp"></a>M</strong></p>
</td>
</tr>
<tr id="row404mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p406mcpsimp"><a name="p406mcpsimp"></a><a name="p406mcpsimp"></a>MCipher</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p408mcpsimp"><a name="p408mcpsimp"></a><a name="p408mcpsimp"></a>Multi-channel Cipher module</p>
</td>
</tr>
<tr id="row409mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p411mcpsimp"><a name="p411mcpsimp"></a><a name="p411mcpsimp"></a>MSID</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p413mcpsimp"><a name="p413mcpsimp"></a><a name="p413mcpsimp"></a>MarketSegmentID.</p>
</td>
</tr>
<tr id="row414mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p416mcpsimp"><a name="p416mcpsimp"></a><a name="p416mcpsimp"></a><strong id="b417mcpsimp"><a name="b417mcpsimp"></a><a name="b417mcpsimp"></a>O</strong></p>
</td>
</tr>
<tr id="row418mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p420mcpsimp"><a name="p420mcpsimp"></a><a name="p420mcpsimp"></a>OS</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p422mcpsimp"><a name="p422mcpsimp"></a><a name="p422mcpsimp"></a>Operating System</p>
</td>
</tr>
<tr id="row423mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p425mcpsimp"><a name="p425mcpsimp"></a><a name="p425mcpsimp"></a>OEM</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p427mcpsimp"><a name="p427mcpsimp"></a><a name="p427mcpsimp"></a>Original Equipment Manufacturer</p>
</td>
</tr>
<tr id="row428mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p430mcpsimp"><a name="p430mcpsimp"></a><a name="p430mcpsimp"></a>OTP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p432mcpsimp"><a name="p432mcpsimp"></a><a name="p432mcpsimp"></a>One Time Programmable</p>
</td>
</tr>
<tr id="row433mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p435mcpsimp"><a name="p435mcpsimp"></a><a name="p435mcpsimp"></a><strong id="b436mcpsimp"><a name="b436mcpsimp"></a><a name="b436mcpsimp"></a>R</strong></p>
</td>
</tr>
<tr id="row437mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p439mcpsimp"><a name="p439mcpsimp"></a><a name="p439mcpsimp"></a>REE</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p441mcpsimp"><a name="p441mcpsimp"></a><a name="p441mcpsimp"></a>Rich Execution Environment</p>
</td>
</tr>
<tr id="row442mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p444mcpsimp"><a name="p444mcpsimp"></a><a name="p444mcpsimp"></a>RKP</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p446mcpsimp"><a name="p446mcpsimp"></a><a name="p446mcpsimp"></a>Root Key Process</p>
</td>
</tr>
<tr id="row447mcpsimp"><td class="cellrowborder" colspan="2" valign="top"><p id="p449mcpsimp"><a name="p449mcpsimp"></a><a name="p449mcpsimp"></a><strong id="b450mcpsimp"><a name="b450mcpsimp"></a><a name="b450mcpsimp"></a>S</strong></p>
</td>
</tr>
<tr id="row451mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p453mcpsimp"><a name="p453mcpsimp"></a><a name="p453mcpsimp"></a>SCS</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p455mcpsimp"><a name="p455mcpsimp"></a><a name="p455mcpsimp"></a>Secure Chipset Startup</p>
</td>
</tr>
<tr id="row456mcpsimp"><td class="cellrowborder" valign="top" width="16%"><p id="p458mcpsimp"><a name="p458mcpsimp"></a><a name="p458mcpsimp"></a>SMC</p>
</td>
<td class="cellrowborder" valign="top" width="84%"><p id="p460mcpsimp"><a name="p460mcpsimp"></a><a name="p460mcpsimp"></a>Secure Monitor Call</p>
</td>
</tr>
</tbody>
</table>
