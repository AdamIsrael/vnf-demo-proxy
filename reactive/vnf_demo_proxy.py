from charms.reactive import when, when_not, set_state


@when_not('vnf-demo-proxy.installed')
def install_vnf_demo_proxy():
    set_state('vnf-demo-proxy.installed')
