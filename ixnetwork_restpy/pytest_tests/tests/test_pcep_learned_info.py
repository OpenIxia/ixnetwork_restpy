def test_gen_nodes_for_pcep_learned_info_update(ixnetwork):
    try:
        # pcc group should be generated
        pcc_group = ixnetwork.Topology.DeviceGroup.Ethernet.Ipv4.Pce.PccGroup
        learned_info_update = pcc_group.LearnedInfoUpdate
        print(learned_info_update.PceBasicRsvpSyncLspUpdateParams.__dir__())
        print(learned_info_update.PceBasicSrSyncLspUpdateParams.__dir__())
        print(learned_info_update.PceBasicSrv6SyncLspUpdateParams.__dir__())
        print(learned_info_update.PceDetailedRsvpSyncLspUpdateParams.__dir__())
        print(learned_info_update.PceDetailedSrSyncLspUpdateParams.__dir__())
        print(learned_info_update.PceDetailedSrv6SyncLspUpdateParams.__dir__())
    except Exception as e:
        err_msg = (
            "pcc_group and all nodes related to learnedInfo should be generated, \nexception: "
            + str(e)
        )
        raise Exception(err_msg)
