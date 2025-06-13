from flask import Flask, render_template, request, redirect, url_for
from controllers.cliente_controller import ClienteController
from controllers.venda_controller import VendaController
from controllers.veiculo_controller import VeiculoController
from controllers.prestador_controller import PrestadorController
from controllers.despesa_controller import DespesaController
from controllers.compra_controller import CompraController
import config

# Configuração do Flask para localizar os templates na estrutura correta
app = Flask(__name__,
            template_folder='templates')

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# ----- CLIENTE -----
@app.route('/clientes')
def listar_clientes():
    clientes = ClienteController.listar()
    return render_template('listar_clientes.html', clientes=clientes)

@app.route('/clientes/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        cidade = request.form['cidade']
        uf = request.form['uf']
        cep = request.form['cep']
        
        ClienteController.cadastrar(nome, endereco, cidade, uf, cep)
        return redirect('/clientes')
    
    return render_template('cliente_form.html')

# ----- PRESTADOR -----
@app.route('/prestadores')
def listar_prestadores():
    prestadores = PrestadorController.listar()
    return render_template('listar_prestadores.html', prestadores=prestadores)

@app.route('/prestadores/cadastrar', methods=['GET', 'POST'])
def cadastrar_prestador():
    if request.method == 'POST':
        nome_empresa = request.form['nome_empresa']
        cidade = request.form['cidade']
        uf = request.form['uf']
        cep = request.form['cep']
        forma_pagamento = request.form['forma_pagamento']
        
        PrestadorController.cadastrar(nome_empresa, cidade, uf, cep, forma_pagamento)
        return redirect('/prestadores')
    
    return render_template('prestador_form.html')

# ----- VEÍCULO -----
@app.route('/veiculos')
def listar_veiculos():
    veiculos = VeiculoController.listar()
    return render_template('listar_veiculos.html', veiculos=veiculos)

@app.route('/veiculos/cadastrar', methods=['GET', 'POST'])
def cadastrar_veiculo():
    if request.method == 'POST':
        idplaca = request.form['idplaca']
        ano = int(request.form['ano'])
        modelo = int(request.form['modelo'])
        preco_fipe = float(request.form['preco_fipe'])
        fabricante = request.form['fabricante']
        modelo_veiculo = request.form['modelo_veiculo']
        cor = request.form['cor']
        preco_venda = float(request.form['preco_venda'])
        
        VeiculoController.cadastrar(idplaca, ano, modelo, preco_fipe, fabricante, modelo_veiculo, cor, preco_venda)
        
        # Se foi informada uma despesa inicial
        if request.form.get('prestador') and request.form.get('descricao') and request.form.get('valor_despesa'):
            prestador = int(request.form['prestador'])
            descricao = request.form['descricao']
            valor_despesa = float(request.form['valor_despesa'])
            data_servico = request.form['data_servico']
            
            DespesaController.cadastrar(idplaca, descricao, valor_despesa, prestador, data_servico)
        
        return redirect('/veiculos')
    
    prestadores = PrestadorController.listar()
    return render_template('veiculo_form.html', prestadores=prestadores)

# ----- DESPESA -----
@app.route('/despesas')
def listar_despesas():
    despesas = DespesaController.listar()
    return render_template('listar_despesas.html', despesas=despesas)

@app.route('/despesas/veiculo/<string:idplaca>')
def listar_despesas_veiculo(idplaca):
    despesas = DespesaController.listar_por_veiculo(idplaca)
    veiculo = VeiculoController.buscar_por_id(idplaca)
    return render_template('despesas_veiculo.html', despesas=despesas, veiculo=veiculo)

@app.route('/despesas/cadastrar', methods=['GET', 'POST'])
def cadastrar_despesa():
    if request.method == 'POST':
        idplaca = request.form['idplaca']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        idprestador = int(request.form['idprestador'])
        data_servico = request.form['data_servico']
        
        DespesaController.cadastrar(idplaca, descricao, valor, idprestador, data_servico)
        return redirect('/despesas')
    
    veiculos = VeiculoController.listar()
    prestadores = PrestadorController.listar()
    return render_template('despesa_form.html', veiculos=veiculos, prestadores=prestadores)

# ----- COMPRA -----
@app.route('/compras')
def listar_compras():
    compras = CompraController.listar()
    return render_template('listar_compras.html', compras=compras)

@app.route('/compras/cadastrar', methods=['GET', 'POST'])
def cadastrar_compra():
    if request.method == 'POST':
        idplaca = request.form['idplaca']
        idcliente = int(request.form['idcliente'])
        data = request.form['data']
        valor_pago = float(request.form['valor_pago'])
        forma_pagamento = request.form['forma_pagamento']
        
        CompraController.cadastrar(idplaca, idcliente, data, valor_pago, forma_pagamento)
        return redirect('/compras')
    
    veiculos = VeiculoController.listar()
    clientes = ClienteController.listar()
    return render_template('compra_form.html', veiculos=veiculos, clientes=clientes)

# ----- VENDA -----
@app.route('/vendas')
def listar_vendas():
    vendas = VendaController.listar()
    return render_template('listar_vendas.html', vendas=vendas)

@app.route('/vendas/cadastrar', methods=['GET', 'POST'])
def cadastrar_venda():
    if request.method == 'POST':
        data = request.form['data']
        idcliente = int(request.form['idcliente'])
        idplaca = request.form.get('idplaca')
        valor_vendido = float(request.form['valor_vendido'])
        forma_pagamento = request.form['forma_pagamento']

        VendaController.cadastrar(data, valor_vendido, idcliente, idplaca, forma_pagamento)
        return redirect('/vendas')

    clientes = ClienteController.listar()
    veiculos = VeiculoController.listar()
    return render_template('venda_form.html', clientes=clientes, veiculos=veiculos)

@app.route('/vendas/<int:idvenda>')
def detalhes_venda(idvenda):
    venda = VendaController.buscar_por_id(idvenda)
    return render_template('detalhes_venda.html', venda=venda, idvenda=idvenda)

if __name__ == '__main__':
    app.run(debug=True)