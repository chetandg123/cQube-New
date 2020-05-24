from HTMLTestRunner import HTMLTestRunner
import unittest

from CRC_Report import Select_District_validate, CRC_District, Anand_Umreth, Bharuch_district, Bhavanagar_test, CRC_download, \
    Cluster_wise_file, CRCreports, dist_blk_clu, Dist_block, District_click_all, District_wise_file, \
    Districtwise_validation, crc_cluster, Kheda_Sandhana_cluster, CRC_Blockwise, Clusterwise_test, cluster_table_record, \
    Navsari_clusters, Footer_data, Rajkot_Jasapur, Select_Type, Selecttype_files, TableData_District, \
    Vansada_cluster, Vasad_blocktest, X_axis, Y_axis, X_Yaxis, CRC_District_Details, Mahesena_Gothva


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        Integration_test = unittest.TestSuite()
        Integration_test.addTests([
             # file name .class name
            unittest.defaultTestLoader.loadTestsFromTestCase(Select_District_validate.Ahmedabad_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_District.Sundalpur_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Anand_Umreth.Umreth_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Bharuch_district.Bharuch_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Bhavanagar_test.Bhavnagar_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_download.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(Cluster_wise_file.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRCreports.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(dist_blk_clu.Ahmedabad_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(Dist_block.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_click_all.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(District_wise_file.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(Districtwise_validation.dwise_type),
            unittest.defaultTestLoader.loadTestsFromTestCase(crc_cluster.Kheda_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Kheda_Sandhana_cluster.Sandhana_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_Blockwise.Mahesana_test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Clusterwise_test.Gothva_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(cluster_table_record.Nav_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Navsari_clusters.Navsari_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Footer_data.Patan_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Rajkot_Jasapur.Jasapur_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Select_Type.Sel_type),
            unittest.defaultTestLoader.loadTestsFromTestCase(Selecttype_files.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(TableData_District.Crc_Reports),
            unittest.defaultTestLoader.loadTestsFromTestCase(Vansada_cluster.Vansada_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(Vasad_blocktest.Valsad_Umbergaon),
            unittest.defaultTestLoader.loadTestsFromTestCase(X_axis.Xaxis),
            unittest.defaultTestLoader.loadTestsFromTestCase(Y_axis.Yaxis),
            unittest.defaultTestLoader.loadTestsFromTestCase(CRC_District_Details.Ahmedabad_report),
            unittest.defaultTestLoader.loadTestsFromTestCase(Mahesena_Gothva.Gothva_cluster),
            unittest.defaultTestLoader.loadTestsFromTestCase(X_Yaxis.XYaxis),
        ])

        outfile = open("/home/chetan/PycharmProjects/cQube/Report/CRC_report.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            verbosity = 1,
            description='Integration Testing of CRC Report'

        )

        runner1.run(Integration_test)

if __name__ == '__main__':
    unittest.main()