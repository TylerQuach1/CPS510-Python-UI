const oracledb = require('oracledb');

oracledb.outFormat = oracledb.OUT_FORMAT_OBJECT;

async function run() {

    const connection = await oracledb.getConnection ({
        user          : "",
        password      : "",
        connectionString : "oracle.scs.ryerson.ca:1521/orcl"
    });

    const result = await connection.execute(
        `SELECT title
         FROM movie`,
        [103],  // bind value for :id
    );

    console.log(result.rows);
    await connection.close();
}

run();