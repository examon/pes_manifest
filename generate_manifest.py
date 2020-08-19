FORTMAT_TEMPLATE = "service-package_evolution_service:{COMPONENT}/{PACKAGE}"


f_manifest = open("pes_manifest.txt", "w")

# Takes list of rpm packages that are in PES pod, formats them and saves to manifest file.
f_pod = open("pes_container_packages.txt", "r")
for i in f_pod:
    res = FORTMAT_TEMPLATE.format(COMPONENT="pes_container", PACKAGE=i.strip())
    f_manifest.write(res + "\n")
f_pod.close()

# Takes list of PES backend packages, formats them and saves to manifest file.
f_backend = open("pes_backend_packages.txt", "r")
for i in f_backend:
    res = FORTMAT_TEMPLATE.format(COMPONENT="pes_backend", PACKAGE=i.strip())
    f_manifest.write(res + "\n")
f_backend.close()

# Takes list of PES frontend packages, formats them and saves to manifest file.
f_frontend = open("pes_frontend_packages.txt", "r")
for i in f_frontend:
    res = FORTMAT_TEMPLATE.format(COMPONENT="pes_frontend", PACKAGE=i.strip())
    f_manifest.write(res + "\n")
f_frontend.close()

# Add dockerfile image
f_manifest.write("Dockerfile-FROM-registry.access.redhat.com/rhel7.6:latest\n")

f_manifest.close()
