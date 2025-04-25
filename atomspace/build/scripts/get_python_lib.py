import sys
import sysconfig
import site

if __name__ == '__main__':
    prefix = sys.argv[1]

    # Use sites if the prefix is recognized and the sites module is available
    # (virtualenv is missing getsitepackages())
    if hasattr(site, 'getsitepackages'):
        paths = [p for p in site.getsitepackages() if p.startswith(prefix)]
        if len(paths) == 1:
            print(paths[0])
            exit(0)
    
    # Use sysconfig platlib as the fall back
    print(sysconfig.get_paths()['platlib'])
