#LDAP RU Lookup
import ldap

server = 'ldap://ldap.ru.ac.za/'
ld = ldap.initialize(server)
ld.simple_bind_s('o=RU')
query = '(&(uid=%s)(objectclass=person))' % ('student number')
results = ld.search_ext_s("o=RU", ldap.SCOPE_SUBTREE, query)
ld.unbind()
print results[0][1]
