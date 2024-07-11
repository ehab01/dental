from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'dentall' # <storage_account_name>
    account_key = 'ORMbrA0VUK+pnHarjwL3yiDmK/C46h7g1D38HFECpqwKLycswd6fkBXSJ77i6/v0HB/67wCq6frz+AStWoulGw==' # <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'dentall' # <storage_account_name>
    account_key = 'ORMbrA0VUK+pnHarjwL3yiDmK/C46h7g1D38HFECpqwKLycswd6fkBXSJ77i6/v0HB/67wCq6frz+AStWoulGw==' # <storage_account_key>
    azure_container = 'static'
    expiration_secs = None