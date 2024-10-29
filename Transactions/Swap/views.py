from django.shortcuts import render
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response
from django.db import connection
# Create your views here.
class CryptoWalletBalanceView(APIView):

    def get(self, request, wallet_id, user_id):
            # SQL query to fetch the balance
            query = """
                SELECT balance
                FROM crypto_wallet_table
                WHERE user_id = %s AND wallet_id = %s
            """

            # Execute the query using a database cursor
            with connection.cursor() as cursor:
                cursor.execute(query, [user_id, wallet_id])
                result = cursor.fetchone()  # Fetch the first result

            # Check if a balance was found and return the result
            if result:
                balance = result[0]  # The balance is the first column in the result
                return Response({'balance': balance})
            else:
                return Response({'error': 'No balance found for this user and wallet'},status=404)
