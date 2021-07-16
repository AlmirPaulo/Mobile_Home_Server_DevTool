#! /usr/bin/env python3 

import main, database, myapp

if __name__ == '__main__':  
   main.app.run(debug=True, port=main.choose_port(main.args.port), host=main.choose_host(main.args.open))
