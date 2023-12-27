import inspect


def check_generator(gen):
    st = inspect.getgeneratorstate(gen)
    if (st == 'GEN_CREATED'): return 'Created'
    elif (st == 'GEN_SUSPENDED'): return 'Started'
    elif (st == 'GEN_CLOSED'): return 'Finished'
    else: return 'Unknow'



gen = (i for i in range(1))
print(gen.__dir__())
print(gen.__getattribute__('gi_frame'))
print(gen.__getattribute__('gi_running'))
print(gen.__getattribute__('gi_yieldfrom'))
print(gen.__getattribute__('gi_code'))
print(inspect.getgeneratorstate(gen))
gen.__next__()
print('-----------------------')
print(gen.__getattribute__('gi_frame'))
print(gen.__getattribute__('gi_running'))
print(gen.__getattribute__('gi_yieldfrom'))
print(gen.__getattribute__('gi_code'))
print(inspect.getgeneratorstate(gen))
try:
    gen.__next__()
except:
    pass
print('-----------------------')
print(gen.__getattribute__('gi_frame'))
print(gen.__getattribute__('gi_running'))
print(gen.__getattribute__('gi_yieldfrom'))
print(gen.__getattribute__('gi_code'))
print(inspect.getgeneratorstate(gen))