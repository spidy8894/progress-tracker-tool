import sqlite3

COMMONTABLE="COMMON_TABLE"

CT_SCOPEDOC="CT_SCOPE_DOC"
CT_APPDOC="CT_APP_DOC"
CT_APPCONFIG_DOC="CT_APP_CONFIG_DOC"
CT_CODE_REPO_ACCESS="CT_CODE_REPO_ACCESS"
CT_CODE_MAVENIZED_AND_EXTERNALIZED="CT_CODE_MAVENIZED_AND_EXTERNALIZED"
CT_LEGACY_SERVER_ACCESS="CT_LEGACY_SERVER_ACCESS"
CT_NEW_VIPS_CREATE_ACCESS="CT_NEW_VIPS_CREATE_ACCESS"
CT_APP_CONFIG_INSTALL_FOR_ALL_ENV="CT_APP_CONFIG_INSTALL_FOR_ALL_ENV"
CT_DNS_ALIESNAME_FOR_ALL_ENVIROMENTS="CT_DNS_ALIESNAME_FOR_ALL_ENVIROMENTS"



DEVTABLE="DEV_TABLE"

DT_CW_MAPPING="DT_CW_MAPPING"
DT_DATA_SOURCE_SET_UP="DT_DATA_SOURCE_SET_UP"
DT_SHARED_LIB_SETUP="DT_SHARED_LIB_SETUP"
DT_DEPLOYED="DT_DEPLOYED"
DT_10PER_TESTCASES="DT_10PER_TESTCASES"
DT_COMPLETED="DT_COMPLETED"

#--------------------------------------------------------------------

class DbConnect:
    def __init__(self statements=None):
        if statements is None:
        statements = []
        
        """Initialize a new or connect to an existing database.

        Accept setup statements to be executed.
        """
         #the database filename
        self.database = 'app.db'
        #holds incomplete statements
        self.statement = ''
        #indicates if selected data is to be returned or printed
        self.display = False

        self.connect()

        #execute setup satements
        self.execute(statements)
        self.close()

    def connect(self):
        """Connect to the SQLite3 database."""

        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.connected = True
        self.statement = ''
        self.close()

    def close(self): 
        """Close the SQLite3 database."""

        self.connection.commit()
        self.connection.close()
        self.connected = False
        
    def incomplete(self, statement):
        """Concatenate clauses until a complete statement is made."""

        self.statement += statement
        if self.statement.count(';') > 1:
            print ('An error has occurerd: ' +
                'You may only execute one statement at a time.')
            print 'For the statement: %s' % self.statement
            self.statement = ''
        if sqlite3.complete_statement(self.statement):
            #the statement is not incomplete, it's complete
            return False
        else:
            #the statement is incomplete
            return True

        

        
        



