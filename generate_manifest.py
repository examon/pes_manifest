FORTMAT_TEMPLATE = "service-package-evolution:{COMPONENT}/{PACKAGE}\n"


def write_packages(package_type, f_write):
    """
    Read list of rpm packages, format them and write to file.
    """
    with open("{}_packages.txt".format(package_type), "r") as f_read:
        for i in f_read:
            res = FORTMAT_TEMPLATE.format(COMPONENT=package_type, PACKAGE=i.strip())
            f_write.write(res)


with open("pes_manifest.txt", "w") as f_manifest:
    # Write rpm packages that are in PES pod to the manifest file.
    write_packages("pes_container", f_manifest)

    # Write PES backend rpm packages to the manifest file.
    write_packages("pes_backend", f_manifest)

    # Write PES frontend rpm packages to the manifest file.
    write_packages("pes_frontend", f_manifest)

    # Add dockerfile image
    f_manifest.write("Dockerfile-FROM-registry.access.redhat.com/rhel7.6:latest\n")
