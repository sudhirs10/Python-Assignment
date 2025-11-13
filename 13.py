# 1
# from flask import Flask, jsonify
# app = Flask(__name__)
# def check_prime(n):
#     if n <= 1:
#         return "No"
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return "No"
#     return "Yes"
# @app.route("/prime_number/<int:number>")
# def prime_number(number):
#     result = check_prime(number)
#     return jsonify({
#         "Number": number,
#         "isPrime": result
#     })
#
# if __name__ == "__main__":
#     app.run(debug=True, host="127.0.0.1", port=5000)

# 2
# from flask import Flask, jsonify
# import mysql.connector
#
#
# DB_CONFIG = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'database': 'airport',
#     'user': 'root',
#     'password': '1010'
# }
#
# app = Flask(__name__)
#
# def get_airport_by_icao(icao_code):
#     try:
#         conn = mysql.connector.connect(**DB_CONFIG)
#         cursor = conn.cursor(dictionary=True)
#         query = """
#         SELECT ident, name, municipality AS city, iso_country AS country
#         FROM airport
#         WHERE ident = %s OR gps_code = %s OR local_code = %s
#         LIMIT 1
#         """
#         cursor.execute(query, (icao_code.upper(), icao_code.upper(), icao_code.upper()))
#         airport = cursor.fetchone()
#         cursor.close()
#         conn.close()
#         return airport
#     except mysql.connector.Error as err:
#         print("Database Error:", err)
#         return None
# @app.route('/airport/<icao>', methods=['GET'])
# def airport_info(icao):
#     airport = get_airport_by_icao(icao)
#     if airport:
#         return jsonify({
#             "ICAO": airport['ident'],
#             "Name": airport['name'],
#             "Location": airport['city'] if airport['city'] else "Unknown",
#             "Country": airport['country']
#         })
#     else:
#         return jsonify({
#             "ICAO": icao.upper(),
#             "error": "Airport not found"
#         }), 404
# if __name__ == '__main__':
#     app.run(debug=True, host='127.0.0.1', port=5000)
