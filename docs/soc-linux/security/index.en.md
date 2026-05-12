---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/en/Security Subsystem User Guide/Security Subsystem User Guide.md
---

# Preface
**Product Version<a name="section18702155413353"></a>**

The product versions corresponding to this document are as follows.

<a name="table187251254193511"></a>
<table><thead align="left"><tr id="row13800185412357"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p1680011544355"><a name="p1680011544355"></a><a name="p1680011544355"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p38006546351"><a name="p38006546351"></a><a name="p38006546351"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row14800754183515"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p680013548356"><a name="p680013548356"></a><a name="p680013548356"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p14800145403519"><a name="p14800145403519"></a><a name="p14800145403519"></a>V100</p>
</td>
</tr>
<tr id="row1814825163714"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p111491650373"><a name="p111491650373"></a><a name="p111491650373"></a>SS626</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p114975173716"><a name="p114975173716"></a><a name="p114975173716"></a>V100</p>
</td>
</tr>
<tr id="row203262171414"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section8711125463519"></a>**

This document (this guide) is mainly intended for the following engineers:

-   Technical support engineers
-   Software development engineers

**Symbol Conventions<a name="section27127546353"></a>**

The following symbols may appear in this document. Their meanings are as follows.

<a name="table18726165483514"></a>
<table><thead align="left"><tr id="row16800195493519"><th class="cellrowborder" valign="top" width="20%" id="mcps1.1.3.1.1"><p id="p178005548352"><a name="p178005548352"></a><a name="p178005548352"></a><strong id="b7800155433510"><a name="b7800155433510"></a><a name="b7800155433510"></a>Symbol</strong></p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.1.3.1.2"><p id="p2800105483516"><a name="p2800105483516"></a><a name="p2800105483516"></a><strong id="b1800554193519"><a name="b1800554193519"></a><a name="b1800554193519"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row880005423516"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p186mcpsimp"><a name="p186mcpsimp"></a><a name="p186mcpsimp"></a><a name="image103"></a><a name="image103"></a><span><img id="image103" src="/soc-linux/security/figures/zh-cn_image_0000002424190174.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.1.3.1.2 "><p id="p58002541356"><a name="p58002541356"></a><a name="p58002541356"></a>Indicates a high-risk hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row9800135483510"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p191mcpsimp"><a name="p191mcpsimp"></a><a name="p191mcpsimp"></a><a name="image104"></a><a name="image104"></a><span><img id="image104" src="/soc-linux/security/figures/zh-cn_image_0000002457868937.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.1.3.1.2 "><p id="p3800145419357"><a name="p3800145419357"></a><a name="p3800145419357"></a>Indicates a medium-risk hazard which, if not avoided, may result in death or serious injury.</p>
</td>
</tr>
<tr id="row1080055419355"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a><a name="image105"></a><a name="image105"></a><span><img id="image105" src="/soc-linux/security/figures/zh-cn_image_0000002457828817.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.1.3.1.2 "><p id="p15801155433513"><a name="p15801155433513"></a><a name="p15801155433513"></a>Indicates a low-risk hazard which, if not avoided, may result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row2801054103511"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p201mcpsimp"><a name="p201mcpsimp"></a><a name="p201mcpsimp"></a><a name="image106"></a><a name="image106"></a><span><img id="image106" src="/soc-linux/security/figures/zh-cn_image_0000002424349998.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.1.3.1.2 "><p id="p128011954183510"><a name="p128011954183510"></a><a name="p128011954183510"></a>Used to convey equipment or environmental safety alert information. If not avoided, it may result in equipment damage, data loss, performance degradation, or other unpredictable results.</p>
<p id="p18010545352"><a name="p18010545352"></a><a name="p18010545352"></a>"Caution" does not involve personal injury.</p>
</td>
</tr>
<tr id="row17801145414351"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p207mcpsimp"><a name="p207mcpsimp"></a><a name="p207mcpsimp"></a><a name="image107"></a><a name="image107"></a><span><img id="image107" src="/soc-linux/security/figures/zh-cn_image_0000002457868929.png" height="27.93" width="75.81"></span></p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.1.3.1.2 "><p id="p16801145418351"><a name="p16801145418351"></a><a name="p16801145418351"></a>Supplemental information to key points in the main text.</p>
<p id="p2801054163520"><a name="p2801054163520"></a><a name="p2801054163520"></a>"Note" is not a safety warning and does not contain information about personal injury, equipment, or environmental damage.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section2467512116410"></a>**

<a name="table256mcpsimp"></a>
<table><thead align="left"><tr id="row262mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.4.1.1"><p id="p264mcpsimp"><a name="p264mcpsimp"></a><a name="p264mcpsimp"></a><strong id="b265mcpsimp"><a name="b265mcpsimp"></a><a name="b265mcpsimp"></a>Document Version</strong></p>
</th>
<th class="cellrowborder" valign="top" width="26%" id="mcps1.1.4.1.2"><p id="p267mcpsimp"><a name="p267mcpsimp"></a><a name="p267mcpsimp"></a><strong id="b268mcpsimp"><a name="b268mcpsimp"></a><a name="b268mcpsimp"></a>Release Date</strong></p>
</th>
<th class="cellrowborder" valign="top" width="53%" id="mcps1.1.4.1.3"><p id="p270mcpsimp"><a name="p270mcpsimp"></a><a name="p270mcpsimp"></a><strong id="b271mcpsimp"><a name="b271mcpsimp"></a><a name="b271mcpsimp"></a>Change Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="row280mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.4.1.1 "><p id="p282mcpsimp"><a name="p282mcpsimp"></a><a name="p282mcpsimp"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="26%" headers="mcps1.1.4.1.2 "><p id="p284mcpsimp"><a name="p284mcpsimp"></a><a name="p284mcpsimp"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="53%" headers="mcps1.1.4.1.3 "><p id="p286mcpsimp"><a name="p286mcpsimp"></a><a name="p286mcpsimp"></a>First temporary version release.</p>
</td>
</tr>
</tbody>
</table>

# Overview
The SSxxxx SoC provides a comprehensive set of security features, including a series of hardware, firmware, and software components to support customers in building secure and trusted devices. The main security features are as follows:

-   One Time Programmable (OTP), used for storing RSA public key hashes for device secure boot verification, multiple groups of symmetric root keys, various SoC security-related control information, and user-defined data.
-   The chip supports three-level key derivation based on OTP symmetric root keys. It supports scrambling protection for root keys burned into OTP. All plaintext keys during the key derivation process are invisible to software.
-   Hardware true random number generator.
-   Asymmetric cryptographic algorithm RSA module.
-   SPACC module supporting multiple general hash algorithms and symmetric cryptographic algorithms.
-   Hardware root-of-trust-based secure boot: supports secure image step-by-step verification; supports optional image encryption; supports TEE/REE trust chain separation; secure boot and non-secure boot images have a unified format, meaning that when secure boot is not enabled, non-encrypted secure boot images can still boot normally.
-   Supports ARM TrustZone, supporting secure and non-secure memory address isolation. Customers can build TEE security solutions.
-   Supports secure JTAG.

# OTP
## Introduction<a name="ZH-CN_TOPIC_0000002457828777"></a>

OTP is a non-volatile memory. Its main characteristic is that once a storage space content is written from 0 to 1, or locked after writing, it cannot be changed again. The SSxxxx OTP includes the following major areas:

1.  Key storage area for various SoC keys: includes storing the root public key hash for secure boot (restricted readable), and storing multiple symmetric cipher algorithm root keys. Once the write operation is initiated on a key area, it locks itself and cannot be changed.

    The chip can store multiple groups of root public key hashes for secure boot verification. These include: chip manufacturer root public key hash (pre-programmed), OEM root public key hash, and third-party dual-signature root public key hash. Customers can select the appropriate root public key based on actual product requirements (via OTP selection).

    Encryption/decryption root keys: The chip reserves 4 OEM-writable symmetric cipher root key OTP spaces, oem\_root\_symc\_key0 through oem\_root\_symc\_key3. OEM can use one or more of these root keys to derive different key encryption keys and working keys. These key areas can be written through the corresponding OTP burning interface. Once written, the hardware locks them automatically and they cannot be changed. The written content cannot be read through software or JTAG interfaces.

    The chip is pre-programmed with one chip manufacturer TEE symmetric cipher algorithm encryption/decryption root key. Users can choose whether to use it based on actual needs (via OTP selection).

2.  SoC important feature/function switch control area (including single-bit control area and multi-bit control area): Most important SoC features can be controlled through OTP to improve product application flexibility. For example: secure boot enable, whether the secure boot image is encrypted, whether secure boot uses redundant backup, whether to enable TEE, JTAG working mode selection, etc. After the target values for the feature/function switch control area are burned, they can be locked to prevent subsequent illegal tampering.

    **It is strongly recommended that customers set all feature/function switch bit values before final product release and force lock them! Even if the default values meet requirements, locking is required.**

3.  User-defined area: The chip integrates approximately 25 Kbits of user-defined OTP area for storing user data.

    The user-defined area also includes a 128-bit version control area: Used for storing important version identifiers to prevent version rollback attacks. That is, preventing attackers from using old legitimate images with security vulnerabilities for re-upgrading, implementing replay attacks. The version control area cannot be locked. Each control bit can only be written from 0 to 1. Once written to 1, it cannot be changed (one-way mode).

    In the SSxxxx SDK package, OTP-related read/write interfaces are provided. For details, refer to the "[SSxxxx OTP Field Definitions](#ZH-CN_TOPIC_0000002457868877)" section and the document "OTP API Reference."

    > **Note:**
    > For all OTP control bits, regardless of whether the default values meet the actual application requirements, please re-burn and lock them all to ensure device security.

## SSxxxx OTP Field Definitions<a name="ZH-CN_TOPIC_0000002457868877"></a>

### OTP Bit Field Attribute Description<a name="ZH-CN_TOPIC_0000002424190150"></a>

#### LOCK Attribute Description<a name="ZH-CN_TOPIC_0000002457828801"></a>

-   **Oneway attribute**: Bit fields with this attribute that have not been burned to 1 can be burned again in subsequent operations until all bits are burned to 1. The lock enable bit does not lock bit fields with this attribute.
-   **lockable attribute**: Bit fields with the lockable attribute behave identically to the oneway attribute before locking. After burning the corresponding lock bit, even bits that have not been burned cannot be burned again. **It is recommended that for lockable attribute bit fields, the corresponding bit fields should be locked after burning the value to prevent modification.**
-   **wrlock attribute**: As long as a write operation has been performed, the corresponding bit field is locked and cannot be changed.

#### Load Shadow Attribute Description<a name="ZH-CN_TOPIC_0000002457868889"></a>

-   After a chip power-on hard reset, OTP values are automatically loaded into the corresponding registers (shadow registers). After each OTP burn, the power must be cycled to read the refreshed values from the shadow registers.
-   OTP bit fields do not have corresponding shadow registers.

### Key Area<a name="ZH-CN_TOPIC_0000002457828785"></a>

<a name="table1869mcpsimp"></a>
<table><thead align="left"><tr id="row1877mcpsimp"><th class="cellrowborder" valign="top" width="28%" id="mcps1.1.6.1.1"><p id="p1879mcpsimp"><a name="p1879mcpsimp"></a><a name="p1879mcpsimp"></a>Field Name</p>
</th>
<th class="cellrowborder" valign="top" width="9%" id="mcps1.1.6.1.2"><p id="p1881mcpsimp"><a name="p1881mcpsimp"></a><a name="p1881mcpsimp"></a>Bit Width</p>
</th>
<th class="cellrowborder" valign="top" width="15%" id="mcps1.1.6.1.3"><p id="p1883mcpsimp"><a name="p1883mcpsimp"></a><a name="p1883mcpsimp"></a>Load Shadow</p>
</th>
<th class="cellrowborder" valign="top" width="9%" id="mcps1.1.6.1.4"><p id="p1885mcpsimp"><a name="p1885mcpsimp"></a><a name="p1885mcpsimp"></a>Lock Attribute</p>
</th>
<th class="cellrowborder" valign="top" width="39%" id="mcps1.1.6.1.5"><p id="p1887mcpsimp"><a name="p1887mcpsimp"></a><a name="p1887mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1889mcpsimp"><td class="cellrowborder" valign="top" width="28%" headers="mcps1.1.6.1.1 "><p id="p1891mcpsimp"><a name="p1891mcpsimp"></a><a name="p1891mcpsimp"></a>oem_root_public_key_sha256</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.2 "><p id="p1893mcpsimp"><a name="p1893mcpsimp"></a><a name="p1893mcpsimp"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="p1895mcpsimp"><a name="p1895mcpsimp"></a><a name="p1895mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.4 "><p id="p1897mcpsimp"><a name="p1897mcpsimp"></a><a name="p1897mcpsimp"></a>wrlock</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.6.1.5 "><p id="p1899mcpsimp"><a name="p1899mcpsimp"></a><a name="p1899mcpsimp"></a>OEM root public key sha256 hash. Used for secure boot trust chain verification.</p>
</td>
</tr>
<tr id="row1900mcpsimp"><td class="cellrowborder" valign="top" width="28%" headers="mcps1.1.6.1.1 "><p id="p1902mcpsimp"><a name="p1902mcpsimp"></a><a name="p1902mcpsimp"></a>tp_root_public_key_sha256</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.2 "><p id="p1904mcpsimp"><a name="p1904mcpsimp"></a><a name="p1904mcpsimp"></a>256</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="p1906mcpsimp"><a name="p1906mcpsimp"></a><a name="p1906mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.4 "><p id="p1908mcpsimp"><a name="p1908mcpsimp"></a><a name="p1908mcpsimp"></a>wrlock</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.6.1.5 "><p id="p1910mcpsimp"><a name="p1910mcpsimp"></a><a name="p1910mcpsimp"></a>Third-party root public key sha256 hash (for secure boot dual signature).</p>
</td>
</tr>
<tr id="row1911mcpsimp"><td class="cellrowborder" valign="top" width="28%" headers="mcps1.1.6.1.1 "><p id="p1913mcpsimp"><a name="p1913mcpsimp"></a><a name="p1913mcpsimp"></a>oem_root_symc_key0</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.2 "><p id="p1915mcpsimp"><a name="p1915mcpsimp"></a><a name="p1915mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="p1917mcpsimp"><a name="p1917mcpsimp"></a><a name="p1917mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.4 "><p id="p1919mcpsimp"><a name="p1919mcpsimp"></a><a name="p1919mcpsimp"></a>wrlock</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.6.1.5 "><p id="p1921mcpsimp"><a name="p1921mcpsimp"></a><a name="p1921mcpsimp"></a>Symmetric algorithm (AES) root key KEY0. Not readable by software.</p>
</td>
</tr>
<tr id="row1922mcpsimp"><td class="cellrowborder" valign="top" width="28%" headers="mcps1.1.6.1.1 "><p id="p1924mcpsimp"><a name="p1924mcpsimp"></a><a name="p1924mcpsimp"></a>oem_root_symc_key1</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.2 "><p id="p1926mcpsimp"><a name="p1926mcpsimp"></a><a name="p1926mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="p1928mcpsimp"><a name="p1928mcpsimp"></a><a name="p1928mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.4 "><p id="p1930mcpsimp"><a name="p1930mcpsimp"></a><a name="p1930mcpsimp"></a>wrlock</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.6.1.5 "><p id="p1932mcpsimp"><a name="p1932mcpsimp"></a><a name="p1932mcpsimp"></a>Symmetric algorithm (AES) root key KEY1. Not readable by software.</p>
</td>
</tr>
<tr id="row1933mcpsimp"><td class="cellrowborder" valign="top" width="28%" headers="mcps1.1.6.1.1 "><p id="p1935mcpsimp"><a name="p1935mcpsimp"></a><a name="p1935mcpsimp"></a>oem_root_symc_key2</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.2 "><p id="p1937mcpsimp"><a name="p1937mcpsimp"></a><a name="p1937mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="p1939mcpsimp"><a name="p1939mcpsimp"></a><a name="p1939mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.4 "><p id="p1941mcpsimp"><a name="p1941mcpsimp"></a><a name="p1941mcpsimp"></a>wrlock</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.6.1.5 "><p id="p1943mcpsimp"><a name="p1943mcpsimp"></a><a name="p1943mcpsimp"></a>Symmetric algorithm (AES) root key KEY2. Not readable by software.</p>
</td>
</tr>
<tr id="row1944mcpsimp"><td class="cellrowborder" valign="top" width="28%" headers="mcps1.1.6.1.1 "><p id="p1946mcpsimp"><a name="p1946mcpsimp"></a><a name="p1946mcpsimp"></a>oem_root_symc_key3</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.2 "><p id="p1948mcpsimp"><a name="p1948mcpsimp"></a><a name="p1948mcpsimp"></a>128</p>
</td>
<td class="cellrowborder" valign="top" width="15%" headers="mcps1.1.6.1.3 "><p id="p1950mcpsimp"><a name="p1950mcpsimp"></a><a name="p1950mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="9%" headers="mcps1.1.6.1.4 "><p id="p1952mcpsimp"><a name="p1952mcpsimp"></a><a name="p1952mcpsimp"></a>wrlock</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.1.6.1.5 "><p id="p1954mcpsimp"><a name="p1954mcpsimp"></a><a name="p1954mcpsimp"></a>Symmetric algorithm (AES) root key KEY3. Not readable by software.</p>
</td>
</tr>
</tbody>
</table>

The key area can be accessed through the following OTP API interface:

```
td_s32 ot_mpi_otp_burn_product_pv(const ot_otp_burn_pv_item *pv, td_u32 num);  td_s32 ot_mpi_otp_read_product_pv(ot_otp_burn_pv_item *pv, td_u32 num);
```

For details, refer to "OTP API Reference."

The content of the key area cannot be read. Therefore, the ot\_mpi\_otp\_read\_product\_pv interface only returns the lock status of the corresponding area (locked areas cannot be written again) and cannot obtain the area content.

### Single-Bit Control Area<a name="ZH-CN_TOPIC_0000002424349982"></a>

<a name="table1960mcpsimp"></a>
<table><thead align="left"><tr id="row1968mcpsimp"><th class="cellrowborder" valign="top" width="21%" id="mcps1.1.6.1.1"><p id="p1970mcpsimp"><a name="p1970mcpsimp"></a><a name="p1970mcpsimp"></a>Field Name</p>
</th>
<th class="cellrowborder" valign="top" width="8%" id="mcps1.1.6.1.2"><p id="p1972mcpsimp"><a name="p1972mcpsimp"></a><a name="p1972mcpsimp"></a>Bit Width</p>
</th>
<th class="cellrowborder" valign="top" width="14%" id="mcps1.1.6.1.3"><p id="p1974mcpsimp"><a name="p1974mcpsimp"></a><a name="p1974mcpsimp"></a>Load Shadow</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.1.6.1.4"><p id="p1976mcpsimp"><a name="p1976mcpsimp"></a><a name="p1976mcpsimp"></a>Lock Attribute</p>
</th>
<th class="cellrowborder" valign="top" width="45%" id="mcps1.1.6.1.5"><p id="p1978mcpsimp"><a name="p1978mcpsimp"></a><a name="p1978mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1980mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p1982mcpsimp"><a name="p1982mcpsimp"></a><a name="p1982mcpsimp"></a>tee_owner_sel</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p1984mcpsimp"><a name="p1984mcpsimp"></a><a name="p1984mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p1986mcpsimp"><a name="p1986mcpsimp"></a><a name="p1986mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p1988mcpsimp"><a name="p1988mcpsimp"></a><a name="p1988mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p1990mcpsimp"><a name="p1990mcpsimp"></a><a name="p1990mcpsimp"></a>Used to select the owner (chip manufacturer/OEM) of the root public key, symmetric key, and TEE-side debug function JTAG key when TEE is enabled. This bit field is invalid when TEE is not enabled.</p>
<p id="p1991mcpsimp"><a name="p1991mcpsimp"></a><a name="p1991mcpsimp"></a>0: OEM (oem_root_public_key_sha256 + oem_root_symc_key0/1/2/3)</p>
<p id="p1992mcpsimp"><a name="p1992mcpsimp"></a><a name="p1992mcpsimp"></a>1: Chip manufacturer</p>
</td>
</tr>
<tr id="row1993mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p1995mcpsimp"><a name="p1995mcpsimp"></a><a name="p1995mcpsimp"></a>oem_rk_deob_en</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p1997mcpsimp"><a name="p1997mcpsimp"></a><a name="p1997mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p1999mcpsimp"><a name="p1999mcpsimp"></a><a name="p1999mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2001mcpsimp"><a name="p2001mcpsimp"></a><a name="p2001mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2003mcpsimp"><a name="p2003mcpsimp"></a><a name="p2003mcpsimp"></a>The chip supports scrambling protection for OTP symmetric root keys. This bit field is used to enable the de-scrambling of OEM_ROOTKEY.</p>
<p id="p2004mcpsimp"><a name="p2004mcpsimp"></a><a name="p2004mcpsimp"></a>0: Disabled;</p>
<p id="p2005mcpsimp"><a name="p2005mcpsimp"></a><a name="p2005mcpsimp"></a>1: Enabled.</p>
</td>
</tr>
<tr id="row2006mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p2008mcpsimp"><a name="p2008mcpsimp"></a><a name="p2008mcpsimp"></a>jtag_key_sel0</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2010mcpsimp"><a name="p2010mcpsimp"></a><a name="p2010mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p2012mcpsimp"><a name="p2012mcpsimp"></a><a name="p2012mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2014mcpsimp"><a name="p2014mcpsimp"></a><a name="p2014mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" rowspan="2" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2016mcpsimp"><a name="p2016mcpsimp"></a><a name="p2016mcpsimp"></a>Root key selection control in functional JTAG password mode.</p>
<p id="p2017mcpsimp"><a name="p2017mcpsimp"></a><a name="p2017mcpsimp"></a>[jtag_key_sel1, jtag_key_sel0]:</p>
<p id="p2018mcpsimp"><a name="p2018mcpsimp"></a><a name="p2018mcpsimp"></a>0x0: Select oem_root_symc_key0 as JTAG root key;</p>
<p id="p2019mcpsimp"><a name="p2019mcpsimp"></a><a name="p2019mcpsimp"></a>0x1: Select oem_root_symc_key1 as JTAG root key;</p>
<p id="p2020mcpsimp"><a name="p2020mcpsimp"></a><a name="p2020mcpsimp"></a>0x2: Select oem_root_symc_key2 as JTAG root key;</p>
<p id="p2021mcpsimp"><a name="p2021mcpsimp"></a><a name="p2021mcpsimp"></a>0x3: Select oem_root_symc_key3 as JTAG root key.</p>
</td>
</tr>
<tr id="row2022mcpsimp"><td class="cellrowborder" valign="top" headers="mcps1.1.6.1.1 "><p id="p2024mcpsimp"><a name="p2024mcpsimp"></a><a name="p2024mcpsimp"></a>jtag_key_sel1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.2 "><p id="p2026mcpsimp"><a name="p2026mcpsimp"></a><a name="p2026mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.3 "><p id="p2028mcpsimp"><a name="p2028mcpsimp"></a><a name="p2028mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.1.6.1.4 "><p id="p2030mcpsimp"><a name="p2030mcpsimp"></a><a name="p2030mcpsimp"></a>lockable</p>
</td>
</tr>
<tr id="row2031mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p2033mcpsimp"><a name="p2033mcpsimp"></a><a name="p2033mcpsimp"></a>sec_ds_enable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2035mcpsimp"><a name="p2035mcpsimp"></a><a name="p2035mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p2037mcpsimp"><a name="p2037mcpsimp"></a><a name="p2037mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2039mcpsimp"><a name="p2039mcpsimp"></a><a name="p2039mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2041mcpsimp"><a name="p2041mcpsimp"></a><a name="p2041mcpsimp"></a>sec_subsys dsensor enable control. When enabled, it enhances the chip's resistance to clock, voltage, and electromagnetic attacks. It is recommended to enable this feature when TEE is enabled.</p>
<p id="p2042mcpsimp"><a name="p2042mcpsimp"></a><a name="p2042mcpsimp"></a>0: Disable sec_subsys dsensor;</p>
<p id="p2043mcpsimp"><a name="p2043mcpsimp"></a><a name="p2043mcpsimp"></a>1: Enable sec_subsys dsensor.</p>
</td>
</tr>
<tr id="row2044mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p2046mcpsimp"><a name="p2046mcpsimp"></a><a name="p2046mcpsimp"></a>acpu_ds_enable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2048mcpsimp"><a name="p2048mcpsimp"></a><a name="p2048mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p2050mcpsimp"><a name="p2050mcpsimp"></a><a name="p2050mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2052mcpsimp"><a name="p2052mcpsimp"></a><a name="p2052mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2054mcpsimp"><a name="p2054mcpsimp"></a><a name="p2054mcpsimp"></a>acpu subsys dsensor enable control. When enabled, it enhances the chip's resistance to clock, voltage, and electromagnetic attacks. It is recommended to enable this feature when TEE is enabled.</p>
<p id="p2055mcpsimp"><a name="p2055mcpsimp"></a><a name="p2055mcpsimp"></a>0: Disable acpu subsys dsensor;</p>
<p id="p2056mcpsimp"><a name="p2056mcpsimp"></a><a name="p2056mcpsimp"></a>1: Enable acpu subsys dsensor.</p>
</td>
</tr>
<tr id="row2057mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p2059mcpsimp"><a name="p2059mcpsimp"></a><a name="p2059mcpsimp"></a>uboot_redundance</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2061mcpsimp"><a name="p2061mcpsimp"></a><a name="p2061mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p2063mcpsimp"><a name="p2063mcpsimp"></a><a name="p2063mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2065mcpsimp"><a name="p2065mcpsimp"></a><a name="p2065mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2067mcpsimp"><a name="p2067mcpsimp"></a><a name="p2067mcpsimp"></a>uboot redundant backup boot enable mode flag.</p>
<p id="p2068mcpsimp"><a name="p2068mcpsimp"></a><a name="p2068mcpsimp"></a>0: Disabled;</p>
<p id="p2069mcpsimp"><a name="p2069mcpsimp"></a><a name="p2069mcpsimp"></a>1: Enabled.</p>
</td>
</tr>
<tr id="row2070mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p2072mcpsimp"><a name="p2072mcpsimp"></a><a name="p2072mcpsimp"></a>otp_pcie_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2074mcpsimp"><a name="p2074mcpsimp"></a><a name="p2074mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p2076mcpsimp"><a name="p2076mcpsimp"></a><a name="p2076mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2078mcpsimp"><a name="p2078mcpsimp"></a><a name="p2078mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2080mcpsimp"><a name="p2080mcpsimp"></a><a name="p2080mcpsimp"></a>PCIE disable control signal, used to turn the PCIE module on/off.</p>
<p id="p2081mcpsimp"><a name="p2081mcpsimp"></a><a name="p2081mcpsimp"></a>0: Enable PCIE;</p>
<p id="p2082mcpsimp"><a name="p2082mcpsimp"></a><a name="p2082mcpsimp"></a>1: Disable PCIE.</p>
</td>
</tr>
<tr id="row2083mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p2085mcpsimp"><a name="p2085mcpsimp"></a><a name="p2085mcpsimp"></a>otp_pcie_ep_boot_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2087mcpsimp"><a name="p2087mcpsimp"></a><a name="p2087mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p2089mcpsimp"><a name="p2089mcpsimp"></a><a name="p2089mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2091mcpsimp"><a name="p2091mcpsimp"></a><a name="p2091mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2093mcpsimp"><a name="p2093mcpsimp"></a><a name="p2093mcpsimp"></a>PCIE endpoint boot disable control signal.</p>
<p id="p2094mcpsimp"><a name="p2094mcpsimp"></a><a name="p2094mcpsimp"></a>0: Enable PCIE endpoint boot mode;</p>
<p id="p2095mcpsimp"><a name="p2095mcpsimp"></a><a name="p2095mcpsimp"></a>1: Disable PCIE endpoint boot mode.</p>
</td>
</tr>
<tr id="row2096mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p2098mcpsimp"><a name="p2098mcpsimp"></a><a name="p2098mcpsimp"></a>bload_dec_en</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2100mcpsimp"><a name="p2100mcpsimp"></a><a name="p2100mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p2102mcpsimp"><a name="p2102mcpsimp"></a><a name="p2102mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2104mcpsimp"><a name="p2104mcpsimp"></a><a name="p2104mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2106mcpsimp"><a name="p2106mcpsimp"></a><a name="p2106mcpsimp"></a>Whether to decrypt the bootloader image for secure boot.</p>
<p id="p2107mcpsimp"><a name="p2107mcpsimp"></a><a name="p2107mcpsimp"></a>0: Whether to decrypt bootloader depends on the Boot_Enc_Flag in the image;</p>
<p id="p2108mcpsimp"><a name="p2108mcpsimp"></a><a name="p2108mcpsimp"></a>1: Decrypt bootloader.</p>
</td>
</tr>
<tr id="row2109mcpsimp"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.1.6.1.1 "><p id="p2111mcpsimp"><a name="p2111mcpsimp"></a><a name="p2111mcpsimp"></a>reserved_flag</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2113mcpsimp"><a name="p2113mcpsimp"></a><a name="p2113mcpsimp"></a>17</p>
</td>
<td class="cellrowborder" valign="top" width="14%" headers="mcps1.1.6.1.3 "><p id="p2115mcpsimp"><a name="p2115mcpsimp"></a><a name="p2115mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2117mcpsimp"><a name="p2117mcpsimp"></a><a name="p2117mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.6.1.5 "><p id="p2119mcpsimp"><a name="p2119mcpsimp"></a><a name="p2119mcpsimp"></a>Reserved flag bits, reserved for custom use.</p>
</td>
</tr>
</tbody>
</table>

The single-bit control area can be accessed through the following OTP API interface:

```
td_s32 ot_mpi_otp_burn_product_pv(const ot_otp_burn_pv_item *pv, td_u32 num);  td_s32 ot_mpi_otp_read_product_pv(ot_otp_burn_pv_item *pv, td_u32 num);
```

For details, refer to "OTP API Reference."

The OTP values of the single-bit control area are reflected in their corresponding shadow registers. The ot\_mpi\_otp\_read\_product\_pv interface only returns the lock status of the control bit (locked positions cannot be written again) and cannot directly obtain the value of the control bit.

### Multi-Bit Control Area<a name="ZH-CN_TOPIC_0000002424349994"></a>

<a name="table2125mcpsimp"></a>
<table><thead align="left"><tr id="row2133mcpsimp"><th class="cellrowborder" valign="top" width="30%" id="mcps1.1.6.1.1"><p id="p2135mcpsimp"><a name="p2135mcpsimp"></a><a name="p2135mcpsimp"></a>Field Name</p>
</th>
<th class="cellrowborder" valign="top" width="8%" id="mcps1.1.6.1.2"><p id="p2137mcpsimp"><a name="p2137mcpsimp"></a><a name="p2137mcpsimp"></a>Bit Width</p>
</th>
<th class="cellrowborder" valign="top" width="13%" id="mcps1.1.6.1.3"><p id="p2139mcpsimp"><a name="p2139mcpsimp"></a><a name="p2139mcpsimp"></a>Load Shadow</p>
</th>
<th class="cellrowborder" valign="top" width="11%" id="mcps1.1.6.1.4"><p id="p2141mcpsimp"><a name="p2141mcpsimp"></a><a name="p2141mcpsimp"></a>Lock Attribute</p>
</th>
<th class="cellrowborder" valign="top" width="37%" id="mcps1.1.6.1.5"><p id="p2143mcpsimp"><a name="p2143mcpsimp"></a><a name="p2143mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row2145mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2147mcpsimp"><a name="p2147mcpsimp"></a><a name="p2147mcpsimp"></a>update_from_uart_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2149mcpsimp"><a name="p2149mcpsimp"></a><a name="p2149mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2151mcpsimp"><a name="p2151mcpsimp"></a><a name="p2151mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2153mcpsimp"><a name="p2153mcpsimp"></a><a name="p2153mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2155mcpsimp"><a name="p2155mcpsimp"></a><a name="p2155mcpsimp"></a>Indicates whether upgrade from UART is allowed.</p>
<p id="p2156mcpsimp"><a name="p2156mcpsimp"></a><a name="p2156mcpsimp"></a>0: Upgrade from UART allowed;</p>
<p id="p2157mcpsimp"><a name="p2157mcpsimp"></a><a name="p2157mcpsimp"></a>1: Upgrade from UART prohibited.</p>
</td>
</tr>
<tr id="row2158mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2160mcpsimp"><a name="p2160mcpsimp"></a><a name="p2160mcpsimp"></a>update_from_sdio_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2162mcpsimp"><a name="p2162mcpsimp"></a><a name="p2162mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2164mcpsimp"><a name="p2164mcpsimp"></a><a name="p2164mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2166mcpsimp"><a name="p2166mcpsimp"></a><a name="p2166mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2168mcpsimp"><a name="p2168mcpsimp"></a><a name="p2168mcpsimp"></a>Indicates whether upgrade from SDIO is allowed.</p>
<p id="p2169mcpsimp"><a name="p2169mcpsimp"></a><a name="p2169mcpsimp"></a>0: Upgrade from SDIO allowed;</p>
<p id="p2170mcpsimp"><a name="p2170mcpsimp"></a><a name="p2170mcpsimp"></a>1: Upgrade from SDIO prohibited.</p>
</td>
</tr>
<tr id="row2171mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2173mcpsimp"><a name="p2173mcpsimp"></a><a name="p2173mcpsimp"></a>update_from_usbdev_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2175mcpsimp"><a name="p2175mcpsimp"></a><a name="p2175mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2177mcpsimp"><a name="p2177mcpsimp"></a><a name="p2177mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2179mcpsimp"><a name="p2179mcpsimp"></a><a name="p2179mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2181mcpsimp"><a name="p2181mcpsimp"></a><a name="p2181mcpsimp"></a>Indicates whether upgrade from USB Device is allowed.</p>
<p id="p2182mcpsimp"><a name="p2182mcpsimp"></a><a name="p2182mcpsimp"></a>0: Upgrade from USB Device allowed;</p>
<p id="p2183mcpsimp"><a name="p2183mcpsimp"></a><a name="p2183mcpsimp"></a>1: Upgrade from USB Device prohibited.</p>
</td>
</tr>
<tr id="row2184mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2186mcpsimp"><a name="p2186mcpsimp"></a><a name="p2186mcpsimp"></a>scs_dbg_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2188mcpsimp"><a name="p2188mcpsimp"></a><a name="p2188mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2190mcpsimp"><a name="p2190mcpsimp"></a><a name="p2190mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2192mcpsimp"><a name="p2192mcpsimp"></a><a name="p2192mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2194mcpsimp"><a name="p2194mcpsimp"></a><a name="p2194mcpsimp"></a>Whether to print debug information when secure boot fails.</p>
<p id="p2195mcpsimp"><a name="p2195mcpsimp"></a><a name="p2195mcpsimp"></a>0: Enable printing;</p>
<p id="p2196mcpsimp"><a name="p2196mcpsimp"></a><a name="p2196mcpsimp"></a>1: Disable printing.</p>
</td>
</tr>
<tr id="row2197mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2199mcpsimp"><a name="p2199mcpsimp"></a><a name="p2199mcpsimp"></a>reserveda0_0</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2201mcpsimp"><a name="p2201mcpsimp"></a><a name="p2201mcpsimp"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2203mcpsimp"><a name="p2203mcpsimp"></a><a name="p2203mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2205mcpsimp"><a name="p2205mcpsimp"></a><a name="p2205mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2207mcpsimp"><a name="p2207mcpsimp"></a><a name="p2207mcpsimp"></a>Reserved</p>
</td>
</tr>
<tr id="row2208mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2210mcpsimp"><a name="p2210mcpsimp"></a><a name="p2210mcpsimp"></a>oem_cw_crc_rd_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2212mcpsimp"><a name="p2212mcpsimp"></a><a name="p2212mcpsimp"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2214mcpsimp"><a name="p2214mcpsimp"></a><a name="p2214mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2216mcpsimp"><a name="p2216mcpsimp"></a><a name="p2216mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2218mcpsimp"><a name="p2218mcpsimp"></a><a name="p2218mcpsimp"></a>Whether to enable CRC of RKP and KLAD calculation results. The driver is provided; keep the default value.</p>
<p id="p2219mcpsimp"><a name="p2219mcpsimp"></a><a name="p2219mcpsimp"></a>0x42: Enable, calculate CRC and CRC result can be read back;</p>
<p id="p2220mcpsimp"><a name="p2220mcpsimp"></a><a name="p2220mcpsimp"></a>Other: Disable, do not calculate CRC.</p>
</td>
</tr>
<tr id="row2221mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2223mcpsimp"><a name="p2223mcpsimp"></a><a name="p2223mcpsimp"></a>func_jtag_prt_mode</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2225mcpsimp"><a name="p2225mcpsimp"></a><a name="p2225mcpsimp"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2227mcpsimp"><a name="p2227mcpsimp"></a><a name="p2227mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2229mcpsimp"><a name="p2229mcpsimp"></a><a name="p2229mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2231mcpsimp"><a name="p2231mcpsimp"></a><a name="p2231mcpsimp"></a>Functional JTAG (for CPU debugging) mode control.</p>
<p id="p2232mcpsimp"><a name="p2232mcpsimp"></a><a name="p2232mcpsimp"></a>0x42: Open;</p>
<p id="p2233mcpsimp"><a name="p2233mcpsimp"></a><a name="p2233mcpsimp"></a>0x63: Password protected;</p>
<p id="p2234mcpsimp"><a name="p2234mcpsimp"></a><a name="p2234mcpsimp"></a>Other: Closed.</p>
</td>
</tr>
<tr id="row2235mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2237mcpsimp"><a name="p2237mcpsimp"></a><a name="p2237mcpsimp"></a>soc_jtag_prt_mode</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2239mcpsimp"><a name="p2239mcpsimp"></a><a name="p2239mcpsimp"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2241mcpsimp"><a name="p2241mcpsimp"></a><a name="p2241mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2243mcpsimp"><a name="p2243mcpsimp"></a><a name="p2243mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2245mcpsimp"><a name="p2245mcpsimp"></a><a name="p2245mcpsimp"></a>DFT JTAG mode control.</p>
<p id="p2246mcpsimp"><a name="p2246mcpsimp"></a><a name="p2246mcpsimp"></a>0x42: Open;</p>
<p id="p2247mcpsimp"><a name="p2247mcpsimp"></a><a name="p2247mcpsimp"></a>0x63: Password protected;</p>
<p id="p2248mcpsimp"><a name="p2248mcpsimp"></a><a name="p2248mcpsimp"></a>Other: Closed.</p>
</td>
</tr>
<tr id="row2249mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2251mcpsimp"><a name="p2251mcpsimp"></a><a name="p2251mcpsimp"></a>uart0_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2253mcpsimp"><a name="p2253mcpsimp"></a><a name="p2253mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2255mcpsimp"><a name="p2255mcpsimp"></a><a name="p2255mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2257mcpsimp"><a name="p2257mcpsimp"></a><a name="p2257mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2259mcpsimp"><a name="p2259mcpsimp"></a><a name="p2259mcpsimp"></a>UART0 port disable control bit.</p>
<p id="p2260mcpsimp"><a name="p2260mcpsimp"></a><a name="p2260mcpsimp"></a>0: Open;</p>
<p id="p2261mcpsimp"><a name="p2261mcpsimp"></a><a name="p2261mcpsimp"></a>1: Closed.</p>
</td>
</tr>
<tr id="row2262mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2264mcpsimp"><a name="p2264mcpsimp"></a><a name="p2264mcpsimp"></a>uart1_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2266mcpsimp"><a name="p2266mcpsimp"></a><a name="p2266mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2268mcpsimp"><a name="p2268mcpsimp"></a><a name="p2268mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2270mcpsimp"><a name="p2270mcpsimp"></a><a name="p2270mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2272mcpsimp"><a name="p2272mcpsimp"></a><a name="p2272mcpsimp"></a>UART1 port disable control bit.</p>
<p id="p2273mcpsimp"><a name="p2273mcpsimp"></a><a name="p2273mcpsimp"></a>0: Open;</p>
<p id="p2274mcpsimp"><a name="p2274mcpsimp"></a><a name="p2274mcpsimp"></a>1: Closed.</p>
</td>
</tr>
<tr id="row2275mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2277mcpsimp"><a name="p2277mcpsimp"></a><a name="p2277mcpsimp"></a>uart2_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2279mcpsimp"><a name="p2279mcpsimp"></a><a name="p2279mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2281mcpsimp"><a name="p2281mcpsimp"></a><a name="p2281mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2283mcpsimp"><a name="p2283mcpsimp"></a><a name="p2283mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2285mcpsimp"><a name="p2285mcpsimp"></a><a name="p2285mcpsimp"></a>UART2 port disable control bit.</p>
<p id="p2286mcpsimp"><a name="p2286mcpsimp"></a><a name="p2286mcpsimp"></a>0: Open;</p>
<p id="p2287mcpsimp"><a name="p2287mcpsimp"></a><a name="p2287mcpsimp"></a>1: Closed.</p>
</td>
</tr>
<tr id="row2288mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2290mcpsimp"><a name="p2290mcpsimp"></a><a name="p2290mcpsimp"></a>uart3_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2292mcpsimp"><a name="p2292mcpsimp"></a><a name="p2292mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2294mcpsimp"><a name="p2294mcpsimp"></a><a name="p2294mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2296mcpsimp"><a name="p2296mcpsimp"></a><a name="p2296mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2298mcpsimp"><a name="p2298mcpsimp"></a><a name="p2298mcpsimp"></a>UART3 port disable control bit.</p>
<p id="p2299mcpsimp"><a name="p2299mcpsimp"></a><a name="p2299mcpsimp"></a>0: Open;</p>
<p id="p2300mcpsimp"><a name="p2300mcpsimp"></a><a name="p2300mcpsimp"></a>1: Closed.</p>
</td>
</tr>
<tr id="row2301mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2303mcpsimp"><a name="p2303mcpsimp"></a><a name="p2303mcpsimp"></a>uart4_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2305mcpsimp"><a name="p2305mcpsimp"></a><a name="p2305mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2307mcpsimp"><a name="p2307mcpsimp"></a><a name="p2307mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2309mcpsimp"><a name="p2309mcpsimp"></a><a name="p2309mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2311mcpsimp"><a name="p2311mcpsimp"></a><a name="p2311mcpsimp"></a>UART4 port disable control bit.</p>
<p id="p2312mcpsimp"><a name="p2312mcpsimp"></a><a name="p2312mcpsimp"></a>0: Open;</p>
<p id="p2313mcpsimp"><a name="p2313mcpsimp"></a><a name="p2313mcpsimp"></a>1: Closed.</p>
</td>
</tr>
<tr id="row2314mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2316mcpsimp"><a name="p2316mcpsimp"></a><a name="p2316mcpsimp"></a>uart5_disable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2318mcpsimp"><a name="p2318mcpsimp"></a><a name="p2318mcpsimp"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2320mcpsimp"><a name="p2320mcpsimp"></a><a name="p2320mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2322mcpsimp"><a name="p2322mcpsimp"></a><a name="p2322mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2324mcpsimp"><a name="p2324mcpsimp"></a><a name="p2324mcpsimp"></a>UART5 port disable control bit.</p>
<p id="p2325mcpsimp"><a name="p2325mcpsimp"></a><a name="p2325mcpsimp"></a>0: Open;</p>
<p id="p2326mcpsimp"><a name="p2326mcpsimp"></a><a name="p2326mcpsimp"></a>1: Closed.</p>
</td>
</tr>
<tr id="row2327mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2329mcpsimp"><a name="p2329mcpsimp"></a><a name="p2329mcpsimp"></a>reserveda1_0</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2331mcpsimp"><a name="p2331mcpsimp"></a><a name="p2331mcpsimp"></a>26</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2333mcpsimp"><a name="p2333mcpsimp"></a><a name="p2333mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2335mcpsimp"><a name="p2335mcpsimp"></a><a name="p2335mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2337mcpsimp"><a name="p2337mcpsimp"></a><a name="p2337mcpsimp"></a>Reserved</p>
</td>
</tr>
<tr id="row2338mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2340mcpsimp"><a name="p2340mcpsimp"></a><a name="p2340mcpsimp"></a>oem_version</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2342mcpsimp"><a name="p2342mcpsimp"></a><a name="p2342mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2344mcpsimp"><a name="p2344mcpsimp"></a><a name="p2344mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2346mcpsimp"><a name="p2346mcpsimp"></a><a name="p2346mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2348mcpsimp"><a name="p2348mcpsimp"></a><a name="p2348mcpsimp"></a>Recommended for use as OEM version number to implement version anti-rollback.</p>
</td>
</tr>
<tr id="row2349mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2351mcpsimp"><a name="p2351mcpsimp"></a><a name="p2351mcpsimp"></a>third_party_version</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2353mcpsimp"><a name="p2353mcpsimp"></a><a name="p2353mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2355mcpsimp"><a name="p2355mcpsimp"></a><a name="p2355mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2357mcpsimp"><a name="p2357mcpsimp"></a><a name="p2357mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2359mcpsimp"><a name="p2359mcpsimp"></a><a name="p2359mcpsimp"></a>Recommended for use as third-party version number to implement version anti-rollback.</p>
</td>
</tr>
<tr id="row2360mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2362mcpsimp"><a name="p2362mcpsimp"></a><a name="p2362mcpsimp"></a>reserved</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2364mcpsimp"><a name="p2364mcpsimp"></a><a name="p2364mcpsimp"></a>384</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2366mcpsimp"><a name="p2366mcpsimp"></a><a name="p2366mcpsimp"></a>N</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2368mcpsimp"><a name="p2368mcpsimp"></a><a name="p2368mcpsimp"></a>oneway</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2370mcpsimp"><a name="p2370mcpsimp"></a><a name="p2370mcpsimp"></a>Reserved</p>
</td>
</tr>
<tr id="row2371mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2373mcpsimp"><a name="p2373mcpsimp"></a><a name="p2373mcpsimp"></a>soc_tee_enable</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2375mcpsimp"><a name="p2375mcpsimp"></a><a name="p2375mcpsimp"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2377mcpsimp"><a name="p2377mcpsimp"></a><a name="p2377mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2379mcpsimp"><a name="p2379mcpsimp"></a><a name="p2379mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2381mcpsimp"><a name="p2381mcpsimp"></a><a name="p2381mcpsimp"></a>Indicates whether TEE is enabled.</p>
<p id="p2382mcpsimp"><a name="p2382mcpsimp"></a><a name="p2382mcpsimp"></a>0x42: TEE disabled. In this case, the CPU defaults to secure state, and TEE and REE are not distinguished.</p>
<p id="p2383mcpsimp"><a name="p2383mcpsimp"></a><a name="p2383mcpsimp"></a>Other: TEE enabled. In TEE environment, the CPU is in secure state; in REE environment, the CPU is in non-secure state.</p>
</td>
</tr>
<tr id="row2384mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2386mcpsimp"><a name="p2386mcpsimp"></a><a name="p2386mcpsimp"></a>reservedlk0</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2388mcpsimp"><a name="p2388mcpsimp"></a><a name="p2388mcpsimp"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2390mcpsimp"><a name="p2390mcpsimp"></a><a name="p2390mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2392mcpsimp"><a name="p2392mcpsimp"></a><a name="p2392mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2394mcpsimp"><a name="p2394mcpsimp"></a><a name="p2394mcpsimp"></a>Reserved</p>
</td>
</tr>
<tr id="row2395mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2397mcpsimp"><a name="p2397mcpsimp"></a><a name="p2397mcpsimp"></a>oem_root_symc_key0_flag</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2399mcpsimp"><a name="p2399mcpsimp"></a><a name="p2399mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2401mcpsimp"><a name="p2401mcpsimp"></a><a name="p2401mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2403mcpsimp"><a name="p2403mcpsimp"></a><a name="p2403mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2405mcpsimp"><a name="p2405mcpsimp"></a><a name="p2405mcpsimp"></a>oem_root_symc_key0 flag.</p>
<p id="p2406mcpsimp"><a name="p2406mcpsimp"></a><a name="p2406mcpsimp"></a>bit[7:0]: Reserved, must be configured as 0x00;</p>
<p id="p2407mcpsimp"><a name="p2407mcpsimp"></a><a name="p2407mcpsimp"></a>bit[8]: deob_key_sel root key scramble static value selection, fixed to 0;</p>
<p id="p2408mcpsimp"><a name="p2408mcpsimp"></a><a name="p2408mcpsimp"></a>bit[9]: root_key_disable current root key slot disable;</p>
<p id="p2409mcpsimp"><a name="p2409mcpsimp"></a><a name="p2409mcpsimp"></a>bit[31:10]: Reserved.</p>
</td>
</tr>
<tr id="row2410mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2412mcpsimp"><a name="p2412mcpsimp"></a><a name="p2412mcpsimp"></a>oem_root_symc_key1_flag</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2414mcpsimp"><a name="p2414mcpsimp"></a><a name="p2414mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2416mcpsimp"><a name="p2416mcpsimp"></a><a name="p2416mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2418mcpsimp"><a name="p2418mcpsimp"></a><a name="p2418mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2420mcpsimp"><a name="p2420mcpsimp"></a><a name="p2420mcpsimp"></a>oem_root_symc_key1 flag.</p>
<p id="p2421mcpsimp"><a name="p2421mcpsimp"></a><a name="p2421mcpsimp"></a>bit[7:0]: Reserved, must be configured as 0x00;</p>
<p id="p2422mcpsimp"><a name="p2422mcpsimp"></a><a name="p2422mcpsimp"></a>bit[8]: deob_key_sel root key scramble static value selection, fixed to 0;</p>
<p id="p2423mcpsimp"><a name="p2423mcpsimp"></a><a name="p2423mcpsimp"></a>bit[9]: root_key_disable current root key slot disable;</p>
<p id="p2424mcpsimp"><a name="p2424mcpsimp"></a><a name="p2424mcpsimp"></a>bit[31:10]: Reserved.</p>
</td>
</tr>
<tr id="row2425mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2427mcpsimp"><a name="p2427mcpsimp"></a><a name="p2427mcpsimp"></a>oem_root_symc_key2_flag</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2429mcpsimp"><a name="p2429mcpsimp"></a><a name="p2429mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2431mcpsimp"><a name="p2431mcpsimp"></a><a name="p2431mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2433mcpsimp"><a name="p2433mcpsimp"></a><a name="p2433mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2435mcpsimp"><a name="p2435mcpsimp"></a><a name="p2435mcpsimp"></a>oem_root_symc_key2 flag.</p>
<p id="p2436mcpsimp"><a name="p2436mcpsimp"></a><a name="p2436mcpsimp"></a>bit[7:0]: Reserved, must be configured as 0x00;</p>
<p id="p2437mcpsimp"><a name="p2437mcpsimp"></a><a name="p2437mcpsimp"></a>bit[8]: deob_key_sel root key scramble static value selection, fixed to 0;</p>
<p id="p2438mcpsimp"><a name="p2438mcpsimp"></a><a name="p2438mcpsimp"></a>bit[9]: root_key_disable current root key slot disable;</p>
<p id="p2439mcpsimp"><a name="p2439mcpsimp"></a><a name="p2439mcpsimp"></a>bit[31:10]: Reserved.</p>
</td>
</tr>
<tr id="row2440mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2442mcpsimp"><a name="p2442mcpsimp"></a><a name="p2442mcpsimp"></a>oem_root_symc_key3_flag</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2444mcpsimp"><a name="p2444mcpsimp"></a><a name="p2444mcpsimp"></a>32</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2446mcpsimp"><a name="p2446mcpsimp"></a><a name="p2446mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2448mcpsimp"><a name="p2448mcpsimp"></a><a name="p2448mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2450mcpsimp"><a name="p2450mcpsimp"></a><a name="p2450mcpsimp"></a>oem_root_symc_key3 flag.</p>
<p id="p2451mcpsimp"><a name="p2451mcpsimp"></a><a name="p2451mcpsimp"></a>bit[7:0]: Reserved, must be configured as 0x00;</p>
<p id="p2452mcpsimp"><a name="p2452mcpsimp"></a><a name="p2452mcpsimp"></a>bit[8]: deob_key_sel root key scramble static value selection, fixed to 0;</p>
<p id="p2453mcpsimp"><a name="p2453mcpsimp"></a><a name="p2453mcpsimp"></a>bit[9]: root_key_disable current root key slot disable;</p>
<p id="p2454mcpsimp"><a name="p2454mcpsimp"></a><a name="p2454mcpsimp"></a>bit[31:10]: Reserved.</p>
</td>
</tr>
<tr id="row2455mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2457mcpsimp"><a name="p2457mcpsimp"></a><a name="p2457mcpsimp"></a>secure_boot_en</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2459mcpsimp"><a name="p2459mcpsimp"></a><a name="p2459mcpsimp"></a>8</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2461mcpsimp"><a name="p2461mcpsimp"></a><a name="p2461mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2463mcpsimp"><a name="p2463mcpsimp"></a><a name="p2463mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2465mcpsimp"><a name="p2465mcpsimp"></a><a name="p2465mcpsimp"></a>Secure boot enable control.</p>
<p id="p2466mcpsimp"><a name="p2466mcpsimp"></a><a name="p2466mcpsimp"></a>0x42: Non-secure boot;</p>
<p id="p2467mcpsimp"><a name="p2467mcpsimp"></a><a name="p2467mcpsimp"></a>Other: Secure boot.</p>
</td>
</tr>
<tr id="row2468mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2470mcpsimp"><a name="p2470mcpsimp"></a><a name="p2470mcpsimp"></a>reservedlk5</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2472mcpsimp"><a name="p2472mcpsimp"></a><a name="p2472mcpsimp"></a>24</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2474mcpsimp"><a name="p2474mcpsimp"></a><a name="p2474mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2476mcpsimp"><a name="p2476mcpsimp"></a><a name="p2476mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2478mcpsimp"><a name="p2478mcpsimp"></a><a name="p2478mcpsimp"></a>Reserved</p>
</td>
</tr>
<tr id="row2479mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2481mcpsimp"><a name="p2481mcpsimp"></a><a name="p2481mcpsimp"></a>double_sign_en</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2483mcpsimp"><a name="p2483mcpsimp"></a><a name="p2483mcpsimp"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2485mcpsimp"><a name="p2485mcpsimp"></a><a name="p2485mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2487mcpsimp"><a name="p2487mcpsimp"></a><a name="p2487mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2489mcpsimp"><a name="p2489mcpsimp"></a><a name="p2489mcpsimp"></a>Secure boot dual signature enable control.</p>
<p id="p2490mcpsimp"><a name="p2490mcpsimp"></a><a name="p2490mcpsimp"></a>0xA: Disabled;</p>
<p id="p2491mcpsimp"><a name="p2491mcpsimp"></a><a name="p2491mcpsimp"></a>Other: Enable dual signature.</p>
</td>
</tr>
<tr id="row2492mcpsimp"><td class="cellrowborder" valign="top" width="30%" headers="mcps1.1.6.1.1 "><p id="p2494mcpsimp"><a name="p2494mcpsimp"></a><a name="p2494mcpsimp"></a>reservedlk6</p>
</td>
<td class="cellrowborder" valign="top" width="8%" headers="mcps1.1.6.1.2 "><p id="p2496mcpsimp"><a name="p2496mcpsimp"></a><a name="p2496mcpsimp"></a>28</p>
</td>
<td class="cellrowborder" valign="top" width="13%" headers="mcps1.1.6.1.3 "><p id="p2498mcpsimp"><a name="p2498mcpsimp"></a><a name="p2498mcpsimp"></a>Y</p>
</td>
<td class="cellrowborder" valign="top" width="11%" headers="mcps1.1.6.1.4 "><p id="p2500mcpsimp"><a name="p2500mcpsimp"></a><a name="p2500mcpsimp"></a>lockable</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.6.1.5 "><p id="p2502mcpsimp"><a name="p2502mcpsimp"></a><a name="p2502mcpsimp"></a>Reserved</p>
</td>
</tr>
</tbody>
</table>

## User-Defined Area<a name="ZH-CN_TOPIC_0000002424190146"></a>

...
