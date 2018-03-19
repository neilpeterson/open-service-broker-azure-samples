from azure.servicebus import ServiceBusService

sbs = ServiceBusService(service_namespace='68f19a00-8c86-4a3d-949c-055ecd3205dd', shared_access_key_name='RootManageSharedAccessKey', shared_access_key_value='S2Cod0nDxa3tE7IAfMGll/C8tLuC4nv9wArxCQEGvLk=')
sbs.send_event('test', 'test')
