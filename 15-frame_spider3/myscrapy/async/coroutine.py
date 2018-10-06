# coding=utf-8
# noinspection PyPackageRequirements
from gevent.monkey import patch_all
# noinspection PyPackageRequirements
from gevent.pool import Pool as BasePool

patch_all()


class Pool(BasePool):

    def apply_async(self, func, args=None, kwds=None, callback=None):
        return super(Pool, self).apply_async(func, args=args, kwds=kwds, callback=callback)

    def close(self):
        pass
