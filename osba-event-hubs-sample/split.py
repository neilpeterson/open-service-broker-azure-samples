event_hub = "Endpoint=sb://eh-1d2aa902-b561-4afd-9407-f1b8fba5cbd1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=S2Cod0nDxa3tE7IAfMGll/C8tLuC4nv9wArxCQEGvLk="
a = event_hub.split(';')
# print(a[0])

eh_nameSpace = (a[0].split('/'))
sbnamespace = eh_nameSpace[2].split('.')[0]
print(sbnamespace)