from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
from conans.tools import os_info, SystemPackageTool
import shutil
import os


class HwlocConan(ConanFile):
    name = "hwloc"
    version = "1.11.13"
    license = "BSD license"
    url = "https://github.com/darcamo/conan-hwloc"
    description = "The Hardware Locality (hwloc) software project aims at easing the process of discovering hardware resources in parallel architectures."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        tools.get("https://download.open-mpi.org/release/hwloc/v1.11/hwloc-{}.tar.gz".format(self.version))
        shutil.move("hwloc-{}".format(self.version), "sources")
        # self.run("git clone https://github.com/memsharded/hello.git")
#         self.run("cd hello && git checkout static_shared")
#         # This small hack might be useful to guarantee proper /MT /MD linkage
#         # in MSVC if the packaged project doesn't have variables to set it
#         # properly
#         tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(MyHello)",
#                               '''PROJECT(MyHello)
# include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()''')

    def build(self):
        autotools = AutoToolsBuildEnvironment(self)
        autotools.configure(configure_dir="sources")
        autotools.make()
        autotools.install()

    # def package(self):
    #     self.copy("*.h", dst="include", src="hello")
    #     self.copy("*hello.lib", dst="lib", keep_path=False)
    #     self.copy("*.dll", dst="bin", keep_path=False)
    #     self.copy("*.so", dst="lib", keep_path=False)
    #     self.copy("*.dylib", dst="lib", keep_path=False)
    #     self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hwloc"]
