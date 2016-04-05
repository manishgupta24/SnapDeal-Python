import requests, json

class Snapdeal:
	def __init__(self, clientId, X_Auth_Token, X_Seller_AuthZ_Token, staging=True):
		
		''' Initialize API Class
		'''

		self.clientId = clientId
		self.X_Auth_Token = X_Auth_Token
		self.X_Seller_AuthZ_Token = X_Seller_AuthZ_Token
		self.staging = staging
		self.session = self.getSession()

	def getSession(self):

		''' Create a session to GET or POST long data sequences. 
		'''
		
		session = requests.Session()
		session.headers.update({
			'clientId': self.clientId,
			'X-Auth-Token': self.X_Auth_Token,
			'X-Seller-AuthZ-Token': self.X_Seller_AuthZ_Token,
		})
		return session

	def searchProducts(self, search_key=None, category_ids=None, brand_ids=None, page_number=None, page_size=None, active=None):
		
		''' Search Seller Products by given filters.
		'''
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/products/search'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/products/search'

		params = {'searchKey':search_key,
				  'categoryIds':category_ids,
				  'brandIds':brand_ids,
				  'pageNumber':page_number,
				  'pageSize':page_size,
				  'active':active}
		return self.session.get(url, params=params)

	def getInventory(self, supc_list):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/products/inventory/bulk'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/products/inventory/bulk'

		supc_string = ','.join(supc_list)
		params = {'supcs':supc_string}
		return self.session.get(url, params=params)

	def postInventory(self, supc_list, inventory_list):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/products/inventory'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/products/inventory'

		payload = []
		for supc, inventory in zip(supc_list, inventory_list):
			payload.append({'supc':supc,
							'availableInventory':inventory})

		return self.session.post(url, data=json.dumps(payload))

	def getPricing(self, supc_list):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/products/price/bulk'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/products/price/bulk'

		supc_string = ','.join(supc_list)
		params = {'supcs':supc_string}
		return self.session.get(url, params=params)

	def postPricing(self, supc_list, mrp_list, selling_price_list):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/products/price'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/products/price'

		payload = []
		for supc, mrp, selling_price in zip(supc_list, mrp_list, selling_price_list):
			payload.append({'supc':supc,
							'mrp':mrp,
							'sellingPrice':sellin_price})

		return self.session.post(url, data=json.dumps(payload))

	def getNewOrders(self, fulfillment_modes_list, page_size=None, page_number=None):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/orders/new'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/orders/new'

		fulfillment_modes = ','.join(fulfillment_modes_list)
		params = {'fModes':fulfillment_modes,
				  'pageSize':page_size,
				  'pageNumber':page_number}

		return self.session.get(url, params=params)

	def getCancelledSubOrders(self, fulfillment_modes_list, page_size=None, page_number=None, start_date=None, end_date=None):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/suborders/cancelled'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/suborders/cancelled'

		fulfillment_modes = ','.join(fulfillment_modes_list)
		params = {'fModes':fulfillment_modes,
				  'pageSize':page_size,
				  'pageNumber':page_number,
				  'startDate':start_date,
				  'endDate':end_date}

		return self.session.get(url, params=params)

	def getCompletedOrders(self, fulfillment_modes_list, page_size=None, page_number=None):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/orders/completed'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/orders/completed'

		fulfillment_modes = ','.join(fulfillment_modes_list)
		params = {'fModes':fulfillment_modes,
				  'pageSize':page_size,
				  'pageNumber':page_number}

		return self.session.get(url, params=params)

	def packnPrintLabels(self, fulfillment_type, order_code_list):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/orders/print'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/orders/print'

		params = {'fulfillmentType':fulfillment_type,
				  'orderCodes':order_code_list}

		return self.session.post(url, params=params)

	def reprintLabels(self, order_code):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/orders/reprint'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/orders/reprint'

		params = {'orderCode':order_code}
		return self.session.post(url, params=params)

	def createOneShipHOS(self, order_code_list):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/oneship/hos'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/oneship/hos'

		params = {'orderCodes':order_code_list}
		return self.session.post(url, params=params)

	def addToOneShipHOS(self, order_code_list, handover_code_id):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/oneship/hos/%s' %order_code
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/oneship/hos/%s' %order_code

		params = {'orderCodes':order_code_list,
				  'id':handover_code_id}

		return self.session.put(url, params=params)

	def printnCloseOneShipHOS(self, handover_code):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/oneship/hos/print'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/oneship/hos/print'

		params = {'handOverCode':handover_code}
		return self.session.post(url, params=params)

	def reprintOneShipHOS(self, handover_code):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/oneship/hos/reprint'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/oneship/hos/reprint'

		params = {'handOverCode':handover_code}
		return self.session.post(url, params=params)
	
	def createDropShipManifest(self, order_code_list):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/dropship/manifest'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/dropship/manifest'

		params = {'orderCodes':order_code_list}
		return self.session.post(url, params=params)

	def addToDropShipHOS(self, order_code_list, handover_code):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/dropship/manifest/%s' %handover_code
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/dropship/manifest/%s' %handover_code

		params = {'orderCodes':order_code_list}
		return self.session.put(url, params=params)

	def printnCloseDropShipHOS(self, handover_code):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/dropship/manifest/print'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/dropship/manifest/print'

		params = {'handOverCode':handover_code}
		return self.session.post(url, params=params)

	def reprintDropShipHOS(self, handover_code):
		if self.staging:
			url = 'http://staging-apigateway.snapdeal.com/seller-api/dropship/manifest/reprint'
		else:
			url = 'https://apigateway.snapdeal.com/seller-api/dropship/manifest/reprint'

		params = {'handOverCode':handover_code}
		return self.session.post(url, params=params)





fulfillment_modes_list = ['VENDOR_SELF','ONESHIP','OCPLUS,DROPSHIP']
supc_list = ['SDL941498120']
inventory_list = [2]
sd = Snapdeal('b1fc52', 'c5589b4426f942e49a63bbbf8ef364e7','7e2ef8cf-d848-43ae-b318-b931a012e1dc', staging=False)
# response = sd.getInventory(supc_list).json()
# response = sd.postInventory(supc_list, inventory_list).json()
response = sd.getNewOrders(fulfillment_modes_list).json()
for each in response['payload']['packages']:
	print each