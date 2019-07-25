import os
import platform
import shutil


class OSInfo:
    def __init__(self, total: int, used: int, free: int,
                 total_human: str, used_human: str, free_human: str, used_percent: float):
        self.total = total
        self.used = used
        self.free = free
        self.total_human = total_human
        self.used_human = used_human
        self.free_human = free_human
        self.used_percent = used_percent

    def __repr__(self):
        return '<OSInfo total={0.total} used={0.used} free={0.free}' \
               ' total_human={0.total_human} used_human={0.used_human}' \
               ' free_human={0.free_human}> used_percent={0.used_percent}'.format(self)


class FileInfo:
    def __init__(self, name: str, bytes: int, human: str, folder: False, created: float):
        self.name = name
        self.bytes = bytes
        self.human = human
        self.folder = folder
        self.created = created

    def __repr__(self):
        return '<FileInfo name={0.name} bytes={0.bytes}' \
               ' human={0.human} folder={0.folder} created={0.created}'.format(self)


class ShowPath:
    def __init__(self, path='.', exclude=None, include_folder=True,
                 human=False, include_stats=True, whitelist=False):
        self.files = {}
        self.path = path
        self.exclude = exclude
        self.human = human
        self.whitelist = whitelist
        self.include_folder = include_folder
        self.include_stats = include_stats

    def readable(self, num, suffix='B'):
        """ Convert Bytes into human readable formats """
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)

    def creation_date(self, filepath):
        """ Returns the timestamp of when the file/folder was created """
        if platform.system() == 'Windows':
            return os.path.getctime(filepath)
        else:
            stat = os.stat(filepath)
            try:
                return stat.st_birthtime
            except AttributeError:
                return stat.st_mtime  # Seems like we're in Linux

    def getOSInfo(self):
        """ Get the current OS Information with disk usage """
        total, used, free = shutil.disk_usage(os.path.abspath(os.getcwd()))

        self.os = OSInfo(
            total, used, free, self.readable(total),
            self.readable(used), self.readable(free),
            round(used / total * 100, 2)
        )

        return self.os

    def getDirectorySize(self, directory):
        """ Search through a directory for all files to then
        find the true size of a folder """
        dir_size = 0
        for (path, dirs, files) in os.walk(directory):
            for file in files:
                filename = os.path.join(path, file)
                try:
                    dir_size += os.path.getsize(filename)
                except FileNotFoundError:
                    dir_size += 0  # Failed to get the size...

        return dir_size

    def getPathFiles(self):
        """ Gets all names and bytes in targeted directory
        and converts them to class FileInfo """
        for i, file in enumerate(os.listdir(self.path)):
            is_folder = False

            try:
                size = os.path.getsize(file)
            except FileNotFoundError:
                print(f"Skipping {file}, unknown file or symlink")

            if not os.path.isfile(file):
                try:
                    is_folder = True
                    size = self.getDirectorySize(file)
                except OSError:
                    print(f"Skipping {file}, no access")
                    continue

            if not self.include_folder and is_folder:
                continue

            try:
                if any([x.lower() in file.lower() for x in self.exclude]):
                    continue
            except TypeError:
                pass

            try:
                if any([x.lower() in file.lower() for x in self.whitelist]):
                    pass
                else:
                    continue
            except TypeError:
                pass

            self.files[i] = FileInfo(
                file, size, self.readable(size),
                is_folder, self.creation_date(file)
            )

        return self.files

    @property
    def all_files(self):
        """ Outputs all files & folders in class FileInfo """
        return list(self.getPathFiles().values())

    @property
    def pretty_print(self, spacing=11):
        """ Outputs all files & folders in a pretty format """
        current_os = self.getOSInfo()
        allFiles = self.all_files

        os_top = f"{'Size'.ljust(spacing)} {'Used'.ljust(spacing)} {'Avail'.ljust(spacing)} {'Use%'.ljust(spacing)}"
        os_bottom = "-" * spacing * 4

        os = "{2}\n{1}\n{0.total_human:<{3}} {0.used_human:<{3}} {0.free_human:<{3}} {0.used_percent}%\n{2}\n".format(
            current_os, os_top, os_bottom, spacing
        )

        files = "\n".join(
            [f"{g.human if self.human else g.bytes:<14} "
            f"{'/' + g.name if g.folder else g.name}"
            for g in sorted(allFiles, key=lambda x: x.bytes, reverse=True)]
        )

        output = files
        if self.include_stats:
            output = os + files

        return output
