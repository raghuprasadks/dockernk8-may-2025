from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
products = {}
current_id = 1

# Create a product
@app.route('/products', methods=['POST'])
def create_product():
    global current_id
    data = request.json
    products[current_id] = {
        'id': current_id,
        'name': data['name'],
        'price': data['price']
    }
    current_id += 1
    return jsonify(products[current_id - 1]), 201

# Read all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(list(products.values()))

# Read a single product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({'error': 'Product not found'}), 404

# Update a product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = products.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    product.update({
        'name': data['name'],
        'price': data['price']
    })
    return jsonify(product)

# Delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return jsonify({'message': 'Product deleted'})
    return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
