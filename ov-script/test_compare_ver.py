import string
import re

class VersionUtils(object):
    @staticmethod
    def maxVersions(versions):
        return VersionUtils.maxList(versions, VersionUtils.compareVersion)

    @staticmethod
    def maxList(theList, fncCompare):
        if len(theList) <= 0:
            return None
        maxVal = theList[0]
        for item in theList[1:]:
            if fncCompare(maxVal, item) < 0:
                maxVal = item
        return maxVal

    @staticmethod
    def maxVersion(ver1, ver2):
        if VersionUtils.compareVersion(ver1, ver2) > 0:
            return ver1
        return ver2

    @staticmethod
    def compareVersion(ver1, ver2):
        arr1, arr2 = VersionUtils.comparableMaker(ver1.split('.'), ver2.split('.'))
        n = len(arr1)

        if VersionUtils.isReleaseVersion(arr1[n - 1]):
            for i in range(0, n - 2):
                if int(arr1[i]) == int(arr2[i]):
                    continue
                return int(arr1[i]) - int(arr2[i])

            l1 = arr1[n - 1]
            l2 = arr2[n - 1]
            compareReleaseVersion = VersionUtils.compareReleaseVersion(l1, l2)
            return compareReleaseVersion if compareReleaseVersion != 0 else int(arr1[n - 2]) - int(arr2[n - 2])

        else:
            for i in range(0, n - 1):
                if int(arr1[i]) == int(arr2[i]):
                    continue
                return int(arr1[i]) - int(arr2[i])

    @staticmethod
    def comparableMaker(arr1, arr2):
        l1 = lr1 = len(arr1)
        l2 = lr2 = len(arr2)
        if VersionUtils.isReleaseVersion(arr1[l1 - 1]):
            lr1 = l1 - 1
        if VersionUtils.isReleaseVersion(arr2[l2 - 1]):
            lr2 = l2 - 1
        mx = max(lr1, lr2)
        arr1 = arr1[:lr1] + ['0'] * (mx - lr1) + [arr1[lr1] if lr1 < l1 else 'R0']
        arr2 = arr2[:lr2] + ['0'] * (mx - lr2) + [arr2[lr2] if lr2 < l2 else 'R0']
        return (arr1, arr2)

    @staticmethod
    def isReleaseVersion(ver):
        return bool(re.match('^[a-zA-Z]\d+$', ver))

    @staticmethod
    def compareReleaseVersion(r1, r2):
        reg1 = re.search('.*[a-zA-Z]+(\d+)', r1)
        reg2 = re.search('.*[a-zA-Z]+(\d+)', r2)
        if reg1 is None:
            if reg2 is None:
                return int(r1) - int(r2)
            else:
                raise ValueError("Incomparable value (%s, %s)" % (r1, r2))
        else:
            if reg2 is None:
                raise ValueError("Incomparable value (%s, %s)" % (r1, r2))
        return int(reg1.group(1)) - int(reg2.group(1))


versions_list = ["8.9.181.R03","8.9.82.R01","8.9.221.R03","8.9.224.R03"]
max_version = VersionUtils.maxVersions(versions_list)
print("Maximum version:", max_version)
