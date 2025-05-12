def test_gen_nodes_for_bgp_vpn_spms(ixnetwork):
    try:
        # pcc group should be generated
        spms_v4 = (
            ixnetwork.Topology.DeviceGroup.NetworkGroup.Ipv4PrefixPools.BgpMVpnSenderSitesIpv4
        )
        print(spms_v4.BgpMVpnSenderSiteSpmsiV4.__dir__())
        print(spms_v4.EvpnIPv4PrefixRange.__dir__())
        print(spms_v4.EvpnIPv6PrefixRange.__dir__())
        print(spms_v4.CMacProperties.__dir__())
        spms_v6 = (
            ixnetwork.Topology.DeviceGroup.NetworkGroup.Ipv6PrefixPools.BgpMVpnSenderSitesIpv6
        )
        print(spms_v6.BgpMVpnSenderSiteSpmsiV6.__dir__())
        print(spms_v6.EvpnIPv4PrefixRange.__dir__())
        print(spms_v6.EvpnIPv6PrefixRange.__dir__())
        print(spms_v6.CMacProperties.__dir__())
    except Exception as e:
        err_msg = (
            "pcc_group and all nodes related to learnedInfo should be generated, \nexception: "
            + str(e)
        )
        raise Exception(err_msg)
