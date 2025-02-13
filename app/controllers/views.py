from flask import request, render_template, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from app.database import create_connection, close_connection
from app.controllers.usuario import Usuario
from functools import wraps

cripto = Bcrypt()


def index():
    return render_template("index.html")


#! tela de Cadastro
def register():
    if request.method == "POST":

        nome = request.form["name"]
        sobrenome = request.form["lastname"]
        email = request.form["email"]
        senha = request.form["password"]
        senha2 = request.form["password2"]

        # * Verificando se as senhas são iguais
        if senha != senha2:
            flash("As senhas não coincidem", "error")
            return render_template("register.html")
        senha_hash = cripto.generate_password_hash(senha).decode("utf-8")

        conexao = create_connection()

        if conexao:
            cursor = conexao.cursor()

            # * Vereficando se o email já está cadastrado no banco de dados
            cursor.execute("SELECT * FROM usuarios WHERE email =%s", (email,))
            existing_email = cursor.fetchone()
            if existing_email:
                flash("O e-mail informado já está sendo utilizado.", "error")
                return render_template("register.html")

        #! salvando dados do usuario no banco de dados
        usuario = Usuario(nome, sobrenome, email, senha_hash)
        usuario.salvar_dados()

        close_connection(conexao)
        return render_template("login.html")
    return render_template("register.html")


#! Tela de Login
def login():
    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["password"]

        conexao = create_connection()

        if conexao:
            cursor = conexao.cursor()
            # * Verificando se o email existe no BD
            cursor.execute("SELECT * FROM usuarios WHERE email =%s", (email,))
            user = cursor.fetchone()

            if user:
                if cripto.check_password_hash(user[4], senha):
                    session["user_id"] = user[0]
                    session["user_name"] = user[1]
                    session["user_lastname"] = user[2]
                    session["user_email"] = user[3]
                    close_connection(conexao)
                    return redirect(url_for("main.dashboard_route"))
                else:
                    flash("Senha incorreta.", "error")

            else:
                flash("E-mail não encontrado", "error")

    return render_template("login.html")


#! Logout
def logout():
    session.clear()
    flash("Desconectado com sucesso", "sucess")
    return redirect(url_for("main.login_route"))


#! Controle de sessão
def controller_session(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            flash("Você precisa estar logado para acessar essa página", "error")
            return redirect(url_for("main.login_route"))
        return f(*args, **kwargs)

    return decorated_function


@controller_session
#! Dashboard
def dashboard():
    return render_template("dashboard.html")
