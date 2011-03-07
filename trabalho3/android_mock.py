# -*- coding: utf-8 -*-
'''
Mock for Android API.

Based on snippet shared on android-script group:

    http://groups.google.com/group/android-scripting/browse_thread/thread/66292c5f5a191a80
'''

class Android (object):
   '''Emulate android API without android.'''

   def __getattr__ (self, name):
       '''Presume that unknown attribute requests are for methods.'''
       def log_method (*args, **kwargs):
           print 'Android.%s ::' % (name,), args, kwargs
       return log_method

   def dialogGetResponse (self, *args, **kwargs):
       class DGR (object):
           def __init__ (self, result='???'):
               self.result = result
       print 'Android.dialogGetResponse ::', args, kwargs
       return DGR ('OK')
