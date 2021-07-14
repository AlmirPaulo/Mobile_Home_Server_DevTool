import main

if __name__ == '__main__':  
   main.app.run(debug=True, port=main.choose_port(main.args.port), host=main.choose_host(main.args.host))
