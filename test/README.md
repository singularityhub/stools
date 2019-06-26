# Example

This is example output for the container built by the recipe in this folder.
From the root directory:


```bash
$ docker build -t vanessa/stools .
$ docker-compose up -d
```

Build the nasty container:

```bash
$ sudo singularity build test/container.sif test/Singularity
```

Then, run the scan!

```bash
$ docker exec -it clair-scanner sclair test/container.sif
```

The output is the following:

```bash
Found 31 Clair namespaces
Clair URL: http://0.0.0.0:6060/v1

1. Starting server...
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)

1. Checking server...
2. Processing images!
Exporting test/container.sif to targz...
INFO:    Starting build...
INFO:    Creating sandbox directory...
INFO:    Build complete: /tmp/tmprnsrtx7z/singularity-clair.atr1vzjm
INFO:    Starting build...
INFO:    Creating sandbox directory...
INFO:    Build complete: /tmp/tmprnsrtx7z/singularity-clair.atr1vzjm
...exported test/container.sif to /tmp/tmprnsrtx7z/singularity-clair.atr1vzjm.gz
...serving http://0.0.0.0:8080/images/singularity-clair.atr1vzjm.gz to Clair
3. Generating report!
db5.3 - 5.3.28-3ubuntu3.1
-------------------------
CVE-2019-8457 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-8457
SQLite3 from 3.6.0 to and including 3.27.2 is vulnerable to heap out-of-bound read in the rtreenode() function when handling invalid rtree tables.


dpkg - 1.17.5ubuntu5.8
----------------------
CVE-2014-8625 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2014-8625
Multiple format string vulnerabilities in the parse_error_msg function in parsehelp.c in dpkg before 1.17.22 allow remote attackers to cause a denial of service (crash) and possibly execute arbitrary code via format string specifiers in the (1) package or (2) architecture name.


CVE-2017-8283 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-8283
dpkg-source in dpkg 1.3.0 through 1.18.23 is able to use a non-GNU patch program and does not offer a protection mechanism for blank-indented diff hunks, which allows remote attackers to conduct directory traversal attacks via a crafted Debian source package, as demonstrated by use of dpkg-source on NetBSD.


bzip2 - 1.0.6-5
---------------
CVE-2016-3189 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-3189
Use-after-free vulnerability in bzip2recover in bzip2 1.0.6 allows remote attackers to cause a denial of service (crash) via a crafted bzip2 file, related to block ends set to before the start of the block.


CVE-2019-12900 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-12900
BZ2_decompress in decompress.c in bzip2 through 1.0.6 has an out-of-bounds write when there are many selectors.


coreutils - 8.21-1ubuntu5.4
---------------------------
CVE-2016-2781 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-2781
chroot in GNU coreutils, when used with --userspec, allows local users to escape to the parent session via a crafted TIOCSTI ioctl call, which pushes characters to the terminal's input buffer.


eglibc - 2.19-0ubuntu6.15
-------------------------
CVE-2019-9192 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-9192
** DISPUTED ** In the GNU C Library (aka glibc or libc6) through 2.29, check_dst_limits_calc_pos_1 in posix/regexec.c has Uncontrolled Recursion, as demonstrated by '(|)(\\1\\1)*' in grep, a different issue than CVE-2018-20796. NOTE: the software maintainer disputes that this is a vulnerability because the behavior occurs only with a crafted pattern.


CVE-2019-7309 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-7309
In the GNU C Library (aka glibc or libc6) through 2.29, the memcmp function for the x32 architecture can incorrectly return zero (indicating that the inputs are equal) because the RDX most significant bit is mishandled.


CVE-2018-6485 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-6485
An integer overflow in the implementation of the posix_memalign in memalign functions in the GNU C Library (aka glibc or libc6) 2.26 and earlier could cause these functions to return a pointer to a heap area that is too small, potentially leading to heap corruption.


CVE-2014-9761 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2014-9761
Multiple stack-based buffer overflows in the GNU C Library (aka glibc or libc6) before 2.23 allow context-dependent attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a long argument to the (1) nan, (2) nanf, or (3) nanl function.


CVE-2017-12132 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12132
The DNS stub resolver in the GNU C Library (aka glibc or libc6) before version 2.26, when EDNS support is enabled, will solicit large UDP responses from name servers, potentially simplifying off-path DNS spoofing attacks due to IP fragmentation.


CVE-2009-5155 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2009-5155
In the GNU C Library (aka glibc or libc6) before 2.28, parse_reg_exp in posix/regcomp.c misparses alternatives, which allows attackers to cause a denial of service (assertion failure and application exit) or trigger an incorrect result by attempting a regular-expression match.


CVE-2014-9984 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2014-9984
nscd in the GNU C Library (aka glibc or libc6) before version 2.20 does not correctly compute the size of an internal buffer when processing netgroup requests, possibly leading to an nscd daemon crash or code execution as the user running nscd.


CVE-2017-12133 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12133
Use-after-free vulnerability in the clntudp_call function in sunrpc/clnt_udp.c in the GNU C Library (aka glibc or libc6) before 2.26 allows remote attackers to have unspecified impact via vectors related to error path.


CVE-2018-20796 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-20796
In the GNU C Library (aka glibc or libc6) through 2.29, check_dst_limits_calc_pos_1 in posix/regexec.c has Uncontrolled Recursion, as demonstrated by '(\227|)(\\1\\1|t1|\\\2537)+' in grep.


CVE-2015-5180 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2015-5180
res_query in libresolv in glibc before 2.25 allows remote attackers to cause a denial of service (NULL pointer dereference and process crash).


CVE-2016-10228 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-10228
The iconv program in the GNU C Library (aka glibc or libc6) 2.25 and earlier, when invoked with the -c option, enters an infinite loop when processing invalid multi-byte input sequences, leading to a denial of service.


libpng - 1.2.50-1ubuntu2.14.04.3
--------------------------------
CVE-2018-14048 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-14048
An issue has been found in libpng 1.6.34. It is a SEGV in the function png_free_data in png.c, related to the recommended error handling for png_read_image.


libbsd - 0.6.0-2ubuntu1
-----------------------
CVE-2016-2090 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-2090
Off-by-one vulnerability in the fgetwln function in libbsd before 0.8.2 allows attackers to have unspecified impact via unknown vectors, which trigger a heap-based buffer overflow.


sudo - 1.8.9p5-1ubuntu1.4
-------------------------
CVE-2016-7076 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-7076
sudo before version 1.8.18p1 is vulnerable to a bypass in the sudo noexec restriction if application run via sudo executed wordexp() C library function with a user supplied argument. A local user permitted to run such application via sudo with noexec restriction could possibly use this flaw to execute arbitrary commands with elevated privileges.


CVE-2016-7032 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-7032
sudo_noexec.so in Sudo before 1.8.15 on Linux might allow local users to bypass intended noexec command restrictions via an application that calls the (1) system or (2) popen function.


CVE-2017-1000368 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-1000368
Todd Miller's sudo version 1.8.20p1 and earlier is vulnerable to an input validation (embedded newlines) in the get_process_ttyname() function resulting in information disclosure and command execution.


CVE-2015-5602 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2015-5602
sudoedit in Sudo before 1.8.15 allows local users to gain privileges via a symlink attack on a file whose full path is defined using multiple wildcards in /etc/sudoers, as demonstrated by "/home/*/*/file.txt."


CVE-2015-8239 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2015-8239
The SHA-2 digest support in the sudoers plugin in sudo after 1.8.7 allows local users with write permissions to parts of the called command to replace them before it is executed.


heimdal - 1.6~git20131207+dfsg-1ubuntu1.2
-----------------------------------------
CVE-2017-6594 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-6594
The transit path validation code in Heimdal before 7.3 might allow attackers to bypass the capath policy protection mechanism by leveraging failure to add the previous hop realm to the transit path of issued tickets.


CVE-2019-12098 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-12098
In the client side of Heimdal before 7.6.0, failure to verify anonymous PKINIT PA-PKINIT-KX key exchange permits a man-in-the-middle attack. This issue is in krb5_init_creds_step in lib/krb5/init_creds_pw.c.


binutils - 2.24-5ubuntu14.2
---------------------------
CVE-2017-7299 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7299
The Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, has an invalid read (of size 8) because the code to emit relocs (bfd_elf_final_link function in bfd/elflink.c) does not check the format of the input file before trying to read the ELF reloc section header. The vulnerability leads to a GNU linker (ld) program crash.


CVE-2017-7224 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7224
The find_nearest_line function in objdump in GNU Binutils 2.28 is vulnerable to an invalid write (of size 1) while disassembling a corrupt binary that contains an empty function name, leading to a program crash.


CVE-2017-9748 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9748
The ieee_object_p function in bfd/ieee.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, might allow remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution. NOTE: this may be related to a compiler bug.


CVE-2017-7301 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7301
The Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, has an aout_link_add_symbols function in bfd/aoutx.h that has an off-by-one vulnerability because it does not carefully check the string offset. The vulnerability could lead to a GNU linker (ld) program crash.


CVE-2017-16830 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-16830
The print_gnu_property_note function in readelf.c in GNU Binutils 2.29.1 does not have integer-overflow protection on 32-bit platforms, which allows remote attackers to cause a denial of service (segmentation violation and application crash) or possibly have unspecified other impact via a crafted ELF file.


CVE-2017-7300 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7300
The Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, has an aout_link_add_symbols function in bfd/aoutx.h that is vulnerable to a heap-based buffer over-read (off-by-one) because of an incomplete check for invalid string offsets while loading symbols, leading to a GNU linker (ld) program crash.


CVE-2018-6323 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-6323
The elf_object_p function in elfcode.h in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29.1, has an unsigned integer overflow because bfd_size_type multiplication is not used. A crafted ELF file allows remote attackers to cause a denial of service (application crash) or possibly have unspecified other impact.


CVE-2017-9040 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9040
GNU Binutils 2017-04-03 allows remote attackers to cause a denial of service (NULL pointer dereference and application crash), related to the process_mips_specific function in readelf.c, via a crafted ELF file that triggers a large memory-allocation attempt.


CVE-2017-9043 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9043
readelf.c in GNU Binutils 2017-04-12 has a "shift exponent too large for type unsigned long" issue, which might allow remote attackers to cause a denial of service (application crash) or possibly have unspecified other impact via a crafted ELF file.


CVE-2017-9747 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9747
The ieee_archive_p function in bfd/ieee.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, might allow remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution. NOTE: this may be related to a compiler bug.


CVE-2017-12455 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12455
The evax_bfd_print_emh function in vms-alpha.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause an out of bounds heap read via a crafted vms alpha file.


CVE-2017-12799 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12799
The elf_read_notesfunction in bfd/elf.c in GNU Binutils 2.29 allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file.


CVE-2017-9755 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9755
opcodes/i386-dis.c in GNU Binutils 2.28 does not consider the number of registers for bnd mode, which allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-7223 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7223
GNU assembler in GNU Binutils 2.28 is vulnerable to a global buffer overflow (of size 1) while attempting to unget an EOF character from the input stream, potentially leading to a program crash.


CVE-2017-12448 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12448
The bfd_cache_close function in bfd/cache.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause a heap use after free and possibly achieve code execution via a crafted nested archive file. This issue occurs because incorrect functions are called during an attempt to release memory. The issue can be addressed by better input validation in the bfd_generic_archive_p function in bfd/archive.c.


CVE-2017-7614 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7614
elflink.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, has a "member access within null pointer" undefined behavior issue, which might allow remote attackers to cause a denial of service (application crash) or possibly have unspecified other impact via an "int main() {return 0;}" program.


CVE-2017-9751 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9751
opcodes/rl78-decode.opc in GNU Binutils 2.28 has an unbounded GETBYTE macro, which allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-14333 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-14333
The process_version_sections function in readelf.c in GNU Binutils 2.29 allows attackers to cause a denial of service (Integer Overflow, and hang because of a time-consuming loop) or possibly have unspecified other impact via a crafted binary file with invalid values of ent.vn_next, during "readelf -a" execution.


CVE-2017-9745 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9745
The _bfd_vms_slurp_etir function in bfd/vms-alpha.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-12456 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12456
The read_symbol_stabs_debugging_info function in rddbg.c in GNU Binutils 2.29 and earlier allows remote attackers to cause an out of bounds heap read via a crafted binary file.


CVE-2017-9753 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9753
The versados_mkobject function in bfd/versados.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, does not initialize a certain data structure, which allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-16828 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-16828
The display_debug_frames function in dwarf.c in GNU Binutils 2.29.1 allows remote attackers to cause a denial of service (integer overflow and heap-based buffer over-read, and application crash) or possibly have unspecified other impact via a crafted ELF file, related to print_debug_frame.


CVE-2017-13716 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13716
The C++ symbol demangler routine in cplus-dem.c in libiberty, as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (excessive memory allocation and application crash) via a crafted file, as demonstrated by a call from the Binary File Descriptor (BFD) library (aka libbfd).


CVE-2017-12454 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12454
The _bfd_vms_slurp_egsd function in bfd/vms-alpha.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause an arbitrary memory read via a crafted vms alpha file.


CVE-2017-9752 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9752
bfd/vms-alpha.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file in the _bfd_vms_get_value and _bfd_vms_slurp_etir functions during "objdump -D" execution.


CVE-2017-14130 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-14130
The _bfd_elf_parse_attributes function in elf-attrs.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (_bfd_elf_attr_strdup heap-based buffer over-read and application crash) via a crafted ELF file.


CVE-2017-6966 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-6966
readelf in GNU Binutils 2.28 has a use-after-free (specifically read-after-free) error while processing multiple, relocated sections in an MSP430 binary. This is caused by mishandling of an invalid symbol index, and mishandling of state across invocations.


CVE-2017-7302 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7302
The Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, has a swap_std_reloc_out function in bfd/aoutx.h that is vulnerable to an invalid read (of size 4) because of missing checks for relocs that could not be recognised. This vulnerability causes Binutils utilities like strip to crash.


CVE-2017-9749 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9749
The *regs* macros in opcodes/bfin-dis.c in GNU Binutils 2.28 allow remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-6965 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-6965
readelf in GNU Binutils 2.28 writes to illegal addresses while processing corrupt input files containing symbol-difference relocations, leading to a heap-based buffer overflow.


CVE-2016-2226 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-2226
Integer overflow in the string_appends function in cplus-dem.c in libiberty allows remote attackers to execute arbitrary code via a crafted executable, which triggers a buffer overflow.


CVE-2017-9041 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9041
GNU Binutils 2.28 allows remote attackers to cause a denial of service (heap-based buffer over-read and application crash) via a crafted ELF file, related to MIPS GOT mishandling in the process_mips_specific function in readelf.c.


CVE-2018-6759 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-6759
The bfd_get_debug_link_info_1 function in opncls.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.30, has an unchecked strnlen operation. Remote attackers could leverage this vulnerability to cause a denial of service (segmentation fault) via a crafted ELF file.


CVE-2017-7227 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7227
GNU linker (ld) in GNU Binutils 2.28 is vulnerable to a heap-based buffer overflow while processing a bogus input script, leading to a program crash. This relates to lack of '\0' termination of a name field in ldlex.l.


CVE-2014-9939 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2014-9939
ihex.c in GNU Binutils before 2.26 contains a stack buffer overflow when printing bad bytes in Intel Hex objects.


CVE-2017-12449 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12449
The _bfd_vms_save_sized_string function in vms-misc.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause an out of bounds heap read via a crafted vms file.


CVE-2017-9044 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9044
The print_symbol_for_build_attribute function in readelf.c in GNU Binutils 2017-04-12 allows remote attackers to cause a denial of service (invalid read and SEGV) via a crafted ELF file.


CVE-2017-9742 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9742
The score_opcodes function in opcodes/score7-dis.c in GNU Binutils 2.28 allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-16826 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-16826
The coff_slurp_line_table function in coffcode.h in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29.1, allows remote attackers to cause a denial of service (invalid memory access and application crash) or possibly have unspecified other impact via a crafted PE file.


CVE-2017-16829 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-16829
The _bfd_elf_parse_gnu_properties function in elf-properties.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29.1, does not prevent negative pointers, which allows remote attackers to cause a denial of service (out-of-bounds read and application crash) or possibly have unspecified other impact via a crafted ELF file.


CVE-2017-16827 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-16827
The aout_get_external_symbols function in aoutx.h in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29.1, allows remote attackers to cause a denial of service (slurp_symtab invalid free and application crash) or possibly have unspecified other impact via a crafted ELF file.


CVE-2017-13710 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13710
The setup_group function in elf.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (NULL pointer dereference and application crash) via a group section that is too small.


CVE-2017-6969 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-6969
readelf in GNU Binutils 2.28 is vulnerable to a heap-based buffer over-read while processing corrupt RL78 binaries. The vulnerability can trigger program crashes. It may lead to an information leak as well.


CVE-2017-9746 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9746
The disassemble_bytes function in objdump.c in GNU Binutils 2.28 allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of rae insns printing for this file during "objdump -D" execution.


CVE-2017-12458 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12458
The nlm_swap_auxiliary_headers_in function in bfd/nlmcode.h in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause an out of bounds heap read via a crafted nlm file.


CVE-2017-9955 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9955
The get_build_id function in opncls.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, allows remote attackers to cause a denial of service (heap-based buffer over-read and application crash) via a crafted file in which a certain size field is larger than a corresponding data field, as demonstrated by mishandling within the objdump program.


CVE-2017-9750 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9750
opcodes/rx-decode.opc in GNU Binutils 2.28 lacks bounds checks for certain scale arrays, which allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-7226 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7226
The pe_ILF_object_p function in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, is vulnerable to a heap-based buffer over-read of size 4049 because it uses the strlen function instead of strnlen, leading to program crashes in several utilities such as addr2line, size, and strings. It could lead to information disclosure as well.


CVE-2017-9039 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9039
GNU Binutils 2.28 allows remote attackers to cause a denial of service (memory consumption) via a crafted ELF file with many program headers, related to the get_program_headers function in readelf.c.


CVE-2017-12967 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12967
The getsym function in tekhex.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29, allows remote attackers to cause a denial of service (stack-based buffer over-read and application crash) via a malformed tekhex binary.


CVE-2017-7209 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7209
The dump_section_as_bytes function in readelf in GNU Binutils 2.28 accesses a NULL pointer while reading section contents in a corrupt binary, leading to a program crash.


CVE-2017-12453 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12453
The _bfd_vms_slurp_eeom function in libbfd.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause an out of bounds heap read via a crafted vms alpha file.


CVE-2018-9996 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-9996
An issue was discovered in cplus-dem.c in GNU libiberty, as distributed in GNU Binutils 2.30. Stack Exhaustion occurs in the C++ demangling functions provided by libiberty, and there are recursive stack frames: demangle_template_value_parm, demangle_integral_value, and demangle_expression.


CVE-2017-9744 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9744
The sh_elf_set_mach_from_flags function in bfd/elf32-sh.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-12459 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12459
The bfd_mach_o_read_symtab_strtab function in bfd/mach-o.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause an out of bounds heap write and possibly achieve code execution via a crafted mach-o file.


CVE-2017-9754 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9754
The process_otr function in bfd/versados.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.28, does not validate a certain offset, which allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-7225 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7225
The find_nearest_line function in addr2line in GNU Binutils 2.28 does not handle the case where the main file name and the directory name are both empty, triggering a NULL pointer dereference and an invalid write, and leading to a program crash.


CVE-2017-12457 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12457
The bfd_make_section_with_flags function in section.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause a NULL dereference via a crafted file.


CVE-2017-16831 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-16831
coffgen.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29.1, does not validate the symbol count, which allows remote attackers to cause a denial of service (integer overflow and application crash, or excessive memory allocation) or possibly have unspecified other impact via a crafted PE file.


CVE-2017-9756 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9756
The aarch64_ext_ldst_reglist function in opcodes/aarch64-dis.c in GNU Binutils 2.28 allows remote attackers to cause a denial of service (buffer overflow and application crash) or possibly have unspecified other impact via a crafted binary file, as demonstrated by mishandling of this file during "objdump -D" execution.


CVE-2017-12452 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12452
The bfd_mach_o_i386_canonicalize_one_reloc function in bfd/mach-o-i386.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause an out of bounds heap read via a crafted mach-o file.


CVE-2017-12450 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12450
The alpha_vms_object_p function in bfd/vms-alpha.c in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29 and earlier, allows remote attackers to cause an out of bounds heap write and possibly achieve code execution via a crafted vms alpha file.


CVE-2017-7210 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7210
objdump in GNU Binutils 2.28 is vulnerable to multiple heap-based buffer over-reads (of size 1 and size 8) while handling corrupt STABS enum type strings in a crafted object file, leading to program crash.


CVE-2017-16832 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-16832
The pe_bfd_read_buildid function in peicode.h in the Binary File Descriptor (BFD) library (aka libbfd), as distributed in GNU Binutils 2.29.1, does not validate size and offset values in the data dictionary, which allows remote attackers to cause a denial of service (segmentation violation and application crash) or possibly have unspecified other impact via a crafted PE file.


CVE-2017-9038 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9038
GNU Binutils 2.28 allows remote attackers to cause a denial of service (heap-based buffer over-read and application crash) via a crafted ELF file, related to the byte_get_little_endian function in elfcomm.c, the get_unwind_section_word function in readelf.c, and ARM unwind information that contains invalid word offsets.


libxml2 - 2.9.1+dfsg1-3ubuntu4.13
---------------------------------
CVE-2017-8872 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-8872
The htmlParseTryOrFinish function in HTMLparser.c in libxml2 2.9.4 allows attackers to cause a denial of service (buffer over-read) or information disclosure.


openldap - 2.4.31-1+nmu2ubuntu8.5
---------------------------------
CVE-2017-14159 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-14159
slapd in OpenLDAP 2.4.45 and earlier creates a PID file after dropping privileges to a non-root account, which might allow local users to kill arbitrary processes by leveraging access to this non-root account for PID file modification before a root script executes a "kill `cat /pathname`" command, as demonstrated by openldap-initscript.


cron - 3.0pl1-124ubuntu2
------------------------
CVE-2017-9525 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-9525
In the cron package through 3.0pl1-128 on Debian, and through 3.0pl1-128ubuntu2 on Ubuntu, the postinst maintainer script allows for group-crontab-to-root privilege escalation via symlink attacks against unsafe usage of the chown and chmod programs.


apache2 - 2.4.7-1ubuntu4.22
---------------------------
CVE-2016-4975 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-4975
Possible CRLF injection allowing HTTP response splitting attacks for sites which use mod_userdir. This issue was mitigated by changes made in 2.4.25 and 2.2.32 which prohibit CR or LF injection into the "Location" or other outbound header key or value. Fixed in Apache HTTP Server 2.4.25 (Affected 2.4.1-2.4.23). Fixed in Apache HTTP Server 2.2.32 (Affected 2.2.0-2.2.31).


util-linux - 2.20.1-5.1ubuntu20.9
---------------------------------
CVE-2014-9114 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2014-9114
Blkid in util-linux before 2.26rc-1 allows local users to execute arbitrary code.


CVE-2016-5011 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-5011
The parse_dos_extended function in partitions/dos.c in the libblkid library in util-linux allows physically proximate attackers to cause a denial of service (memory consumption) via a crafted MSDOS partition table with an extended partition boot record at zero offset.


CVE-2013-0157 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2013-0157
(a) mount and (b) umount in util-linux 2.14.1, 2.17.2, and probably other versions allow local users to determine the existence of restricted directories by (1) using the --guess-fstype command-line option or (2) attempting to mount a non-existent device, which generates different error messages depending on whether the directory exists.


mpfr4 - 3.1.2-1
---------------
CVE-2014-9474 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2014-9474
Buffer overflow in the mpfr_strtofr function in GNU MPFR before 3.1.2-p11 allows context-dependent attackers to have unspecified impact via vectors related to incorrect documentation for mpn_set_str.


dbus - 1.6.18-0ubuntu4.5
------------------------
CVE-2019-12749 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-12749
dbus before 1.10.28, 1.12.x before 1.12.16, and 1.13.x before 1.13.12, as used in DBusServer in Canonical Upstart in Ubuntu 14.04 (and in some, less common, uses of dbus-daemon), allows cookie spoofing because of symlink mishandling in the reference implementation of DBUS_COOKIE_SHA1 in the libdbus library. (This only affects the DBUS_COOKIE_SHA1 authentication mechanism.) A malicious client with write access to its own home directory could manipulate a ~/.dbus-keyrings symlink to cause a DBusServer with a different uid to read and write in unintended locations. In the worst case, this could result in the DBusServer reusing a cookie that is known to the malicious client, and treating that cookie as evidence that a subsequent client connection came from an attacker-chosen uid, allowing authentication bypass.


openssl - 1.0.1f-1ubuntu2.27
----------------------------
CVE-2019-1559 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-1559
If an application encounters a fatal protocol error and then calls SSL_shutdown() twice (once to send a close_notify, and once to receive one) then OpenSSL can respond differently to the calling application if a 0 byte record is received with invalid padding compared to if a 0 byte record is received with an invalid MAC. If the application then behaves differently based on that in a way that is detectable to the remote peer, then this amounts to a padding oracle that could be used to decrypt data. In order for this to be exploitable "non-stitched" ciphersuites must be in use. Stitched ciphersuites are optimised implementations of certain commonly used ciphersuites. Also the application must call SSL_shutdown() twice even if a protocol error has occurred (applications should not do this but some do anyway). Fixed in OpenSSL 1.0.2r (Affected 1.0.2-1.0.2q).


ncurses - 5.9+20140118-1ubuntu1
-------------------------------
CVE-2017-11112 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-11112
In ncurses 6.0, there is an attempted 0xffffffffffffffff access in the append_acs function of tinfo/parse_entry.c. It could lead to a remote denial of service attack if the terminfo library code is used to process untrusted terminfo data.


CVE-2017-13734 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13734
There is an illegal address access in the _nc_safe_strcat function in strings.c in ncurses 6.0 that will lead to a remote denial of service attack.


CVE-2017-16879 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-16879
Stack-based buffer overflow in the _nc_write_entry function in tinfo/write_entry.c in ncurses 6.0 allows attackers to cause a denial of service (application crash) or possibly execute arbitrary code via a crafted terminfo file, as demonstrated by tic.


CVE-2017-13733 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13733
There is an illegal address access in the fmt_entry function in progs/dump_entry.c in ncurses 6.0 that might lead to a remote denial of service attack.


CVE-2017-10685 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-10685
In ncurses 6.0, there is a format string vulnerability in the fmt_entry function. A crafted input will lead to a remote arbitrary code execution attack.


CVE-2017-13732 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13732
There is an illegal address access in the function dump_uses() in progs/dump_entry.c in ncurses 6.0 that might lead to a remote denial of service attack.


CVE-2017-10684 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-10684
In ncurses 6.0, there is a stack-based buffer overflow in the fmt_entry function. A crafted input will lead to a remote arbitrary code execution attack.


CVE-2017-13730 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13730
There is an illegal address access in the function _nc_read_entry_source() in progs/tic.c in ncurses 6.0 that might lead to a remote denial of service attack.


CVE-2017-13728 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13728
There is an infinite loop in the next_char function in comp_scan.c in ncurses 6.0, related to libtic. A crafted input will lead to a remote denial of service attack.


CVE-2017-13729 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13729
There is an illegal address access in the _nc_save_str function in alloc_entry.c in ncurses 6.0. It will lead to a remote denial of service attack.


CVE-2017-11113 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-11113
In ncurses 6.0, there is a NULL Pointer Dereference in the _nc_parse_entry function of tinfo/parse_entry.c. It could lead to a remote denial of service attack if the terminfo library code is used to process untrusted terminfo data.


CVE-2017-13731 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13731
There is an illegal address access in the function postprocess_termcap() in parse_entry.c in ncurses 6.0 that will lead to a remote denial of service attack.


libtasn1-6 - 3.4-3ubuntu0.6
---------------------------
CVE-2018-1000654 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-1000654
GNU Libtasn1-4.13 libtasn1-4.13 version libtasn1-4.13, libtasn1-4.12 contains a DoS, specifically CPU usage will reach 100% when running asn1Paser against the POC due to an issue in _asn1_expand_object_id(p_tree), after a long time, the program will be killed. This attack appears to be exploitable via parsing a crafted file.


python3.4 - 3.4.3-1ubuntu1~14.04.7
----------------------------------
CVE-2019-9947 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-9947
An issue was discovered in urllib2 in Python 2.x through 2.7.16 and urllib in Python 3.x through 3.7.3. CRLF injection is possible if the attacker controls a url parameter, as demonstrated by the first argument to urllib.request.urlopen with \r\n (specifically in the path component of a URL that lacks a ? character) followed by an HTTP header or a Redis command. This is similar to the CVE-2019-9740 query string issue.


CVE-2019-5010 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-5010
NULL pointer dereference using a specially crafted X509 certificate


CVE-2019-9740 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-9740
An issue was discovered in urllib2 in Python 2.x through 2.7.16 and urllib in Python 3.x through 3.7.3. CRLF injection is possible if the attacker controls a url parameter, as demonstrated by the first argument to urllib.request.urlopen with \r\n (specifically in the query string after a ? character) followed by an HTTP header or a Redis command.


CVE-2018-20406 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-20406
Modules/_pickle.c in Python before 3.7.1 has an integer overflow via a large LONG_BINPUT value that is mishandled during a "resize to twice the size" attempt. This issue might cause memory exhaustion, but is only relevant if the pickle format is used for serializing tens or hundreds of gigabytes of data.


CVE-2019-9636 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-9636
Python 2.7.x through 2.7.16 and 3.x through 3.7.2 is affected by: Improper Handling of Unicode Encoding (with an incorrect netloc) during NFKC normalization. The impact is: Information disclosure (credentials, cookies, etc. that are cached against a given hostname). The components are: urllib.parse.urlsplit, urllib.parse.urlparse. The attack vector is: A specially crafted URL could be incorrectly parsed to locate cookies or authentication data and send that information to a different host than when parsed correctly.


ntp - 1:4.2.6.p5+dfsg-3ubuntu2.14.04.13
---------------------------------------
CVE-2018-12327 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-12327
Stack-based buffer overflow in ntpq and ntpdc of NTP version 4.2.8p11 allows an attacker to achieve code execution or escalate to higher privileges via a long string as the argument for an IPv4 or IPv6 command-line parameter. NOTE: It is unclear whether there are any common situations in which ntpq or ntpdc is used with a command line from an untrusted source.


CVE-2018-7170 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-7170
ntpd in ntp 4.2.x before 4.2.8p7 and 4.3.x before 4.3.92 allows authenticated users that know the private symmetric key to create arbitrarily-many ephemeral associations in order to win the clock selection of ntpd and modify a victim's clock via a Sybil attack. This issue exists because of an incomplete fix for CVE-2016-1549.


patch - 2.7.1-4ubuntu2.4
------------------------
CVE-2018-6952 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-6952
A double free exists in the another_hunk function in pch.c in GNU patch through 2.7.6.


apr-util - 1.5.3-1
------------------
CVE-2017-12618 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12618
Apache Portable Runtime Utility (APR-util) 1.6.0 and prior fail to validate the integrity of SDBM database files used by apr_sdbm*() functions, resulting in a possible out of bound read access. A local user with write access to the database can make a program or process using these functions crash, and cause a denial of service.


sqlite3 - 3.8.2-1ubuntu2.2
--------------------------
CVE-2017-2518 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-2518
An issue was discovered in certain Apple products. iOS before 10.3.2 is affected. macOS before 10.12.5 is affected. tvOS before 10.2.1 is affected. watchOS before 3.2.2 is affected. The issue involves the "SQLite" component. It allows remote attackers to execute arbitrary code or cause a denial of service (buffer overflow and application crash) via a crafted SQL statement.


CVE-2017-10989 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-10989
The getNodeSize function in ext/rtree/rtree.c in SQLite through 3.19.3, as used in GDAL and other products, mishandles undersized RTree blobs in a crafted database, leading to a heap-based buffer over-read or possibly unspecified other impact.


CVE-2019-8457 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-8457
SQLite3 from 3.6.0 to and including 3.27.2 is vulnerable to heap out-of-bound read in the rtreenode() function when handling invalid rtree tables.


CVE-2017-13685 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-13685
The dump_callback function in SQLite 3.20.0 allows remote attackers to cause a denial of service (EXC_BAD_ACCESS and application crash) via a crafted file.


CVE-2018-20506 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-20506
SQLite before 3.25.3, when the FTS3 extension is enabled, encounters an integer overflow (and resultant buffer overflow) for FTS3 queries in a "merge" operation that occurs after crafted changes to FTS3 shadow tables, allowing remote attackers to execute arbitrary code by leveraging the ability to run arbitrary SQL statements (such as in certain WebSQL use cases). This is a different vulnerability than CVE-2018-20346.


CVE-2016-6153 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-6153
os_unix.c in SQLite before 3.13.0 improperly implements the temporary directory search algorithm, which might allow local users to obtain sensitive information, cause a denial of service (application crash), or have unspecified other impact by leveraging use of the current working directory for temporary files.


CVE-2019-5827 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-5827
[Unknown description]


CVE-2018-20346 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-20346
SQLite before 3.25.3, when the FTS3 extension is enabled, encounters an integer overflow (and resultant buffer overflow) for FTS3 queries that occur after crafted changes to FTS3 shadow tables, allowing remote attackers to execute arbitrary code by leveraging the ability to run arbitrary SQL statements (such as in certain WebSQL use cases), aka Magellan.


vim - 2:7.4.052-1ubuntu3.1
--------------------------
CVE-2017-11109 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-11109
Vim 8.0 allows attackers to cause a denial of service (invalid free) or possibly have unspecified other impact via a crafted source (aka -S) file. NOTE: there might be a limited number of scenarios in which this has security relevance.


CVE-2017-6349 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-6349
An integer overflow at a u_read_undo memory allocation site would occur for vim before patch 8.0.0377, if it does not properly validate values for tree length when reading a corrupted undo file, which may lead to resultant buffer overflows.


CVE-2017-6350 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-6350
An integer overflow at an unserialize_uep memory allocation site would occur for vim before patch 8.0.0378, if it does not properly validate values for tree length when reading a corrupted undo file, which may lead to resultant buffer overflows.


CVE-2017-5953 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-5953
vim before patch 8.0.0322 does not properly validate values for tree length when handling a spell file, which may result in an integer overflow at a memory allocation site and a resultant buffer overflow.


CVE-2017-17087 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-17087
fileio.c in Vim prior to 8.0.1263 sets the group ownership of a .swp file to the editor's primary group (which may be different from the group ownership of the original file), which allows local users to obtain sensitive information by leveraging an applicable group membership, as demonstrated by /etc/shadow owned by root:shadow mode 0640, but /etc/.shadow.swp owned by root:users mode 0640, a different vulnerability than CVE-2017-1000382.


zlib - 1:1.2.8.dfsg-1ubuntu1.1
------------------------------
CVE-2016-9843 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-9843
The crc32_big function in crc32.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact via vectors involving big-endian CRC calculation.


CVE-2016-9842 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-9842
The inflateMark function in inflate.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact via vectors involving left shifts of negative integers.


CVE-2016-9841 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-9841
inffast.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact by leveraging improper pointer arithmetic.


CVE-2016-9840 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-9840
inftrees.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact by leveraging improper pointer arithmetic.


pcre3 - 1:8.31-2ubuntu2.3
-------------------------
CVE-2017-7246 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7246
Stack-based buffer overflow in the pcre32_copy_substring function in pcre_get.c in libpcre1 in PCRE 8.40 allows remote attackers to cause a denial of service (WRITE of size 268) or possibly have unspecified other impact via a crafted file.


CVE-2017-7245 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-7245
Stack-based buffer overflow in the pcre32_copy_substring function in pcre_get.c in libpcre1 in PCRE 8.40 allows remote attackers to cause a denial of service (WRITE of size 4) or possibly have unspecified other impact via a crafted file.


systemd - 204-5ubuntu20.31
--------------------------
CVE-2018-20839 (Medium)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-20839
systemd 242 changes the VT1 mode upon a logout, which allows attackers to read cleartext passwords in certain circumstances, such as watching a shutdown, or using Ctrl-Alt-F1 and Ctrl-Alt-F2. This occurs because the KDGKBMODE (aka current keyboard mode) check is mishandled.


gcc-4.8 - 4.8.4-2ubuntu1~14.04.4
--------------------------------
CVE-2015-5276 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2015-5276
The std::random_device class in libstdc++ in the GNU Compiler Collection (aka GCC) before 4.9.4 does not properly handle short reads from blocking sources, which makes it easier for context-dependent attackers to predict the random values via unspecified vectors.


apr - 1.5.0-1
-------------
CVE-2017-12613 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12613
When apr_time_exp*() or apr_os_exp_time*() functions are invoked with an invalid month field value in Apache Portable Runtime APR 1.6.2 and prior, out of bounds memory may be accessed in converting this value to an apr_time_exp_t value, potentially revealing the contents of a different static heap value or resulting in program termination, and may represent an information disclosure or denial of service vulnerability to applications which call these APR functions with unvalidated external input.


shadow - 1:4.1.5.1-1ubuntu9.5
-----------------------------
CVE-2013-4235 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2013-4235
TOCTOU race conditions by copying and removing directory trees


CVE-2017-12424 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2017-12424
In shadow before 4.5, the newusers tool could be made to manipulate internal data structures in ways unintended by the authors. Malformed input may lead to crashes (with a buffer overflow or other memory corruption) or other unspecified behaviors. This crosses a privilege boundary in, for example, certain web-hosting environments in which a Control Panel allows an unprivileged user account to create subaccounts.


CVE-2018-7169 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-7169
An issue was discovered in shadow 4.5. newgidmap (in shadow-utils) is setuid and allows an unprivileged user to be placed in a user namespace where setgroups(2) is permitted. This allows an attacker to remove themselves from a supplementary group, which may allow access to certain filesystem paths if the administrator has used "group blacklisting" (e.g., chmod g-rwx) to restrict access to paths. This flaw effectively reverts a security feature in the kernel (in particular, the /proc/self/setgroups knob) to prevent this sort of privilege escalation.


audit - 1:2.3.2-2ubuntu1
------------------------
CVE-2015-5186 (Negligible)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2015-5186
Audit before 2.4.4 in Linux does not sanitize escape characters in filenames.


tar - 1.27.1-1ubuntu0.1
-----------------------
CVE-2018-20482 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2018-20482
GNU Tar through 1.30, when --sparse is used, mishandles file shrinkage during read access, which allows local users to cause a denial of service (infinite read loop in sparse_dump_region in sparse.c) by modifying a file that is supposed to be archived by a different user's process (e.g., a system backup running as root).
```
