/* Based on TheRainbowPhoenix/Edelweiss payloads/demo.c. Edit edl_main() to build your app. */
#include "edl.h"
#include "ebrew_assets.h"

int edl_main(const struct edl_api *api)
{
    api->rect(0, 0, 528, 320, 0xf7be);
    api->blit(0, 20, 528, 160, edl_wallpaper);
    api->rect(0, 0, 528, 20, 0x3d9b);
    api->text(12, 5, 0xffff, "Edelweiss template example");
    api->text(28, 195, 0x3186, "This wallpaper is 168,960 bytes of loaded ELF data.");
    api->text(28, 218, 0x3186, "It exceeds the original 128 KiB D01 image limit.");
    api->text(28, 244, 0x3186, "Code executes from P1; OS calls use the host bridge.");
    api->text(28, 285, 0x3d9b, "Press any key to return to the launcher.");
    api->present();
    struct edl_event e;
    api->wait(&e);
    return EDL_EXIT;
}
EDL_METADATA const struct edl_metadata edl_meta = {.magic = EDL_ABI_MAGIC,
                                                   .version = 1,
                                                   .title = "Edelweiss example",
                                                   .description =
                                                       "A real payload larger than the D01 buffer",
                                                   .icon = {EDL_DEMO_ICON}};
