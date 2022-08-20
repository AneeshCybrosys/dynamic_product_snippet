import time
from odoo import http
from odoo.http import request


class MostSoldProduct(http.Controller):
    @http.route(['/total_product_sold'], type="json", auth="public",
                website=True)
    def sold_total(self, products_per_slide=4):
        # most sold products
        sale = request.env['sale.order.line'].sudo().search([
            ('state', 'in', ['done', 'sale'])
        ])
        most_sold = sale.product_id.product_tmpl_id.sorted(
            key=lambda x: x.sales_count, reverse=True)
        display_products = []
        for products in most_sold:
            items = \
                products.read(['display_name', 'description_sale', 'list_price',
                               'website_url'])[0]
            items['image'] = request.env['website'].image_url(products,
                                                              'image_512')
            display_products.append(items)

        # most viewed
        viewed = request.env['website.track'].sudo().search(
            [('product_id', '!=', False)])
        most_viewed = viewed.product_id.product_tmpl_id
        most_viewed_products = []
        for products in most_viewed:
            items = \
                products.read(['display_name', 'description_sale', 'list_price',
                               'website_url'])[0]
            items['image'] = request.env['website'].image_url(products,
                                                              'image_512')
            most_viewed_products.append(items)

        # grouping the sold products
        sold_group = []
        sold_list = []
        for index, record in enumerate(display_products, 1):
            sold_list.append(record)
            if index % products_per_slide == 0:
                sold_group.append(sold_list)
                sold_list = []
        if any(sold_list):
            sold_group.append(sold_list)

        # grouping the sold products
        viewed_group = []
        viewed_list = []
        for index, record in enumerate(most_viewed_products, 1):
            viewed_list.append(record)
            if index % products_per_slide == 0:
                viewed_group.append(viewed_list)
                viewed_list = []
        if any(viewed_list):
            viewed_group.append(viewed_list)

        values = {
            "objects": sold_group,
            "most_viewed": viewed_group,
            "products_per_slide": products_per_slide,
            "num_slides": len(sold_group),
            "uniqueId": "pc-%d" % int(time.time() * 1000),
        }
        response = http.Response(
            template='dynamic_product_snippet.basic_snippet', qcontext=values)
        return response.render()
