@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        imagem = request.form['imagem']

        novo = Produto(nome=nome, preco=preco, imagem=imagem)
        db.session.add(novo)
        db.session.commit()

        return redirect('/admin')

    produtos = Produto.query.all()
    return render_template('admin.html', produtos=produtos)