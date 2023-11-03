const oracledb = require('oracledb');

let clientOpts = {};
if (process.platform === 'win32') {                                   // Windows
    clientOpts = { libDir: 'C:\\oracle\\instantclient_21_12' };
} else if (process.platform === 'darwin' && process.arch === 'x64') { // macOS Intel
    clientOpts = { libDir: 'C:\\oracle\\instantclient_21_12' };
} // else on other platforms the system library search path
  // must always be set before Node.js is started.

// enable Thick mode which is needed for SODA
oracledb.initOracleClient(clientOpts);

async function run() {

    const connection = await oracledb.getConnection ({
        user          : "",
        password      : "",
        connectString : "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))",
    });

    const result = await connection.execute(
        `SELECT * FROM movie`
    );

    console.log(result.rows);
    await connection.close();
}

run();