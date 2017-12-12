import ops
import iopc

pkg_path = ""
output_dir = ""
arch = ""
src_usr_lib_dir = ""
src_usr_lib_dir2 = ""
src_usr_bin_dir = ""
dst_lib_dir = ""
dst_usr_bin_dir = ""
src_include_dir = ""
dst_include_dir = ""

def set_global(args):
    global pkg_path
    global output_dir
    global arch
    global src_usr_lib_dir
    global src_usr_lib_dir2
    global src_usr_bin_dir
    global dst_lib_dir
    global dst_usr_bin_dir
    global src_include_dir
    global dst_include_dir
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    arch = ops.getEnv("ARCH_ALT")
    if arch == "armhf":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/arm-linux-gnueabihf")
        src_usr_lib_dir2 = iopc.getBaseRootFile("usr/lib")
        src_usr_bin_dir = iopc.getBaseRootFile("usr/bin")
    elif arch == "armel":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/arm-linux-gnueabi")
        src_usr_lib_dir2 = iopc.getBaseRootFile("usr/lib")
        src_usr_bin_dir = iopc.getBaseRootFile("usr/bin")
    elif arch == "x86_64":
        src_usr_lib_dir = iopc.getBaseRootFile("usr/lib/x86_64-linux-gnu")
        src_usr_lib_dir2 = iopc.getBaseRootFile("usr/lib")
        src_usr_bin_dir = iopc.getBaseRootFile("usr/bin")
    else:
        sys.exit(1)
    dst_lib_dir = ops.path_join(output_dir, "lib")
    dst_usr_bin_dir = ops.path_join(output_dir, "usr/bin")

    src_include_dir = iopc.getBaseRootFile("usr/include")
    dst_include_dir = ops.path_join("include",args["pkg_name"])


def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)

    ops.mkdir(dst_lib_dir)
    ops.copyto(ops.path_join(src_usr_lib_dir, "libtokyocabinet.so.9.11.0"), dst_lib_dir)
    ops.ln(dst_lib_dir, "libtokyocabinet.so.9.11.0", "libtokyocabinet.so.9.11")
    ops.ln(dst_lib_dir, "libtokyocabinet.so.9.11.0", "libtokyocabinet.so.9")
    ops.ln(dst_lib_dir, "libtokyocabinet.so.9.11.0", "libtokyocabinet.so")

    ops.copyto(ops.path_join(src_usr_lib_dir2, "libtokyotyrant.so.3.23.0"), dst_lib_dir)
    ops.ln(dst_lib_dir, "libtokyotyrant.so.3.23.0", "libtokyotyrant.so.3.23")
    ops.ln(dst_lib_dir, "libtokyotyrant.so.3.23.0", "libtokyotyrant.so.3")
    ops.ln(dst_lib_dir, "libtokyotyrant.so.3.23.0", "libtokyotyrant.so")

    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(build_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)
    return False

def MAIN_BUILD(args):
    set_global(args)
    return False

def MAIN_INSTALL(args):
    set_global(args)

    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "tcrdb.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "ttutil.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "tcutil.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "tchdb.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "tcbdb.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "tcfdb.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "tctdb.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(src_include_dir, "tcadb.h"), dst_include_dir)
    iopc.installBin(args["pkg_name"], ops.path_join(dst_lib_dir, "."), "lib") 
    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)
    return False

def MAIN(args):
    set_global(args)

