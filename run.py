from mobile_dev_server import views, control, app

if __name__ == '__main__':  app.run(debug=True, port=control.choose_port(control.args.port))
