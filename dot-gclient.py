solutions = [{
  "managed": False,
  "name": "src/flutter",
  "url": "https://github.com/flutter/engine.git",
  "deps_file": "DEPS",
  "custom_vars": {
    "download_linux_deps": True,
    "download_android_deps": False,
    "download_esbuild": False,
  },
  "custom_deps": {
    "src/flutter/third_party/swiftshader": None,
  }
}]
