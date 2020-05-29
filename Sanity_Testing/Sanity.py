from HTMLTestRunner import HTMLTestRunner
import unittest

from Sanity_Testing import Block_Button_click, Block_details, Click_on_CRCreport, click_on_SR, click_on_TAR, \
    Cluster_Button_click, Cluster_details, Dashboard_click, Dist_blk_cluster_select, District_Block_select, \
    District_choose, Download_click, Home_icon_click, Log_out, login_1, login_2, login_3, login_4_test, login_5_test, \
    login_6_test, login_7_test, login_8_test, login_9_test, login_10_test, login_test, Schools_Btn_click, \
    Schools_details, Url_test


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Sanity_test = unittest.TestSuite()
        Sanity_test.addTests([
             # file name .class name

            unittest.defaultTestLoader.loadTestsFromTestCase(Block_Button_click.Blockbtn_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Block_details.test_blockdetails),
            unittest.defaultTestLoader.loadTestsFromTestCase(Click_on_CRCreport.test_crc),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_SR.test_SR),
            unittest.defaultTestLoader.loadTestsFromTestCase(click_on_TAR.test_TAR),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_Button_click.test_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_details.test_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dashboard_click.test_Dashboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dist_blk_cluster_select.Test_Distbllk),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_Block_select.Test_Distbllk),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_choose.Dist_choose),
            unittest.defaultTestLoader.loadTestsFromTestCase(Download_click.test_download),
            unittest.defaultTestLoader.loadTestsFromTestCase(Home_icon_click.test_homeicon),
            unittest.defaultTestLoader.loadTestsFromTestCase(Log_out.test_logout),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_1.url_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_2.login_2_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_3.login_3_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_4_test.login_3_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_5_test.login_5_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_6_test.login_6_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_7_test.login_7_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_8_test.login_8_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_9_test.login_9_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_10_test.login_10_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(login_test.login_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schools_Btn_click.school_btn),
            unittest.defaultTestLoader.loadTestsFromTestCase(Schools_details.school_details),
            unittest.defaultTestLoader.loadTestsFromTestCase(Url_test.url_test),
        ])
        # report = pwd()
        outfile = open("/home/chetan/cQube-New/Reports/sanity_Report.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Sanity Test Result '

        )

        runner1.run(Sanity_test)

if __name__ == '__main__':
    unittest.main()