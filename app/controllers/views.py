from flask import request, render_template, redirect, url_for, flash


def index():
    return render_template('index.html')

def register():
    ...
