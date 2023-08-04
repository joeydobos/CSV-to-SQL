 - Converts unformatted data without double quotes ("") into appropriate formats for SQL INSERT statements.
- Automatically recognises if a value is an INT or text and wraps text in double quotes ("") for proper insertion into VARCHAR columns.
- Generates SQL INSERT statements for databases that have only VARCHAR and INT data types.