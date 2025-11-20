import bpy

from .catalog_utils import AssetCatalogFile


def create_brushes_from_images(context, filepaths, b_fake_user):
    print("reading images from %r" % (filepaths))
    extensions = tuple(bpy.path.extensions_image)
    settings = bpy.context.scene.img2brush_settings
    textures = []

    for file in filepaths:
        if not file.lower().endswith(extensions):
            continue

        try:
            image = bpy.data.images.load(file)
        except BaseException as ex:
            print("Failed to load %r, error: %r" % (file, ex))
            break

        image.use_fake_user = b_fake_user

        # Create new texture.
        # NOTE: use the image name instead of `file` in case
        # it's encoding isn't `utf-8` compatible.
        texture = bpy.data.textures.new(image.name, "IMAGE")
        texture.use_fake_user = b_fake_user

        # Assign the image to the texture.
        texture.image = image
        textures.append({"texture": texture, "name": bpy.path.display_name(file)})
        print("imported:", repr(file))

    print("Finished importing images as textures")

    max_value = 0
    for index, brush in enumerate(bpy.data.brushes):
        split_name = brush.name.split(settings.brush_separator)
        digit_found = (
            split_name[-1]
            if split_name[-1].isdigit()
            else split_name[0]
            if split_name[0].isdigit()
            else 0
        )
        if digit_found:
            digit_value = int(digit_found)
            if digit_value > max_value:
                max_value = digit_value

    print("Max existing brush index found:", max_value)

    if (
        settings.create_brush_assets
        and bpy.data.is_saved
        and len(settings.brushes_path) > 0
    ):
        catalog = AssetCatalogFile(bpy.path.abspath("//"), load_from_file=True)
        print("Asset Catalog loaded from:", bpy.path.abspath("//"))
        paths = settings.brushes_path.split("/")
        existing_catalogs = catalog.get_catalogs_from_file()

        uuids = []
        for index, path in enumerate(paths):
            if index == 0:
                uuids.append(catalog.ensure_catalog_exists(path).uuid)

            else:
                print("-".join(paths[: index + 1]))
                if "/".join(paths[: index + 1]) not in existing_catalogs:
                    uuids.append(
                        catalog.ensure_catalog_exists(
                            "-".join(paths[: index + 1]), "/".join(paths[: index + 1])
                        ).uuid
                    )
                else:
                    uuids.append(existing_catalogs["/".join(paths[: index + 1])].uuid)
        catalog.write()

    for index, texture in enumerate(textures):
        brush_name = create_brush_name(texture["name"], max_value + index)
        print("Creating brush asset:", brush_name)
        brush = bpy.data.brushes.new(name=brush_name, mode="SCULPT")
        brush.texture_slot.texture = texture["texture"]
        brush.stroke_method = settings.brush_type
        brush.spacing = settings.brush_spacing
        brush.curve_distance_falloff_preset = settings.brushes_curve

        if settings.create_brush_assets:
            # Set as asset
            brush.asset_mark()

            brush.asset_data.author = "Images to Brushes Add-on"
            brush.asset_data.description = (
                "Brush created from image texture by Images to Brushes Add-on"
            )
            if len(uuids) > 0:
                brush.asset_data.catalog_id = uuids[-1]

        item = bpy.context.scene.created_brushes.add()
        item.brush = brush
        item.selected = False
        print(item.brush, "added to created brushes collection")

    return {"FINISHED"}


def create_brush_name(file_name, index):
    settings = bpy.context.scene.img2brush_settings
    main_name = (
        settings.brush_name if settings.brush_numbering != "ORIGINAL" else file_name
    )
    pad_amount = (
        3
        if settings.brush_numbering == "TWO_ZEROES"
        else 2
        if settings.brush_numbering == "ONE_ZERO"
        else 0
    )
    number_index = (
        f"{(index + 1):0{pad_amount}}" if settings.brush_numbering != "ORIGINAL" else ""
    )
    separator = (
        settings.brush_separator if settings.brush_numbering != "ORIGINAL" else ""
    )
    return (
        (number_index + separator + main_name)
        if settings.brush_numbering_suffix
        else (main_name + separator + number_index)
    )
