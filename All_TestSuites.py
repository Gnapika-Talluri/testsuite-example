import unittest


from testing.Adding_Coupon import Cart_AC
from testing.admin_add_item import Cart_AI
from testing.admin_add_sale_price import Cart_ASP
from testing.admin_delete_item import Cart_ADI
from testing.admin_delete_sale_price import Cart_ADSP
from testing.Checkout_with_Coupon import Cart_CWC
from testing.delete_order_from_cart import Cart_DOFC
from testing.item_in_cart_continue_shopping import Cart_IICCS
from testing.place_an_order_multiple_items import Cart_PAOMI
from testing.place_order import Cart_PO
from testing.Sort_By import Cart_SB
from testing.Two_Different_Item_Order import Cart_TDIO
from testing.Update_Order import Cart_UO

from testing.admin_csv_output import Cart_CSV
from testing.admin_order_detail_view import Cart_AODV
from testing.successful_search import Cart_SS
from testing.search_no_results import Cart_SNR
from testing.successful_payment import Cart_SP
from testing.unsuccessful_payment import Cart_USP

tc1 = unittest.TestLoader().loadTestsFromTestCase(Cart_AC)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Cart_AI)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Cart_ASP)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Cart_ADI)
tc5 = unittest.TestLoader().loadTestsFromTestCase(Cart_ADSP)
tc6 = unittest.TestLoader().loadTestsFromTestCase(Cart_CWC)
tc7 = unittest.TestLoader().loadTestsFromTestCase(Cart_DOFC)
tc8 = unittest.TestLoader().loadTestsFromTestCase(Cart_IICCS)
tc9 = unittest.TestLoader().loadTestsFromTestCase(Cart_PAOMI)
tc10 = unittest.TestLoader().loadTestsFromTestCase(Cart_PO)
tc11 = unittest.TestLoader().loadTestsFromTestCase(Cart_SB)
tc12 = unittest.TestLoader().loadTestsFromTestCase(Cart_TDIO)
tc13 = unittest.TestLoader().loadTestsFromTestCase(Cart_UO)

tc14 = unittest.TestLoader().loadTestsFromTestCase(Cart_CSV)
tc15 = unittest.TestLoader().loadTestsFromTestCase(Cart_AODV)
tc16 = unittest.TestLoader().loadTestsFromTestCase(Cart_SS)
tc17 = unittest.TestLoader().loadTestsFromTestCase(Cart_SNR)
tc18 = unittest.TestLoader().loadTestsFromTestCase(Cart_SP)
tc19 = unittest.TestLoader().loadTestsFromTestCase(Cart_USP)


TestSuite = unittest.TestSuite([tc1, tc14, ])
unittest.TextTestRunner().run(TestSuite)