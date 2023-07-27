
# meta developer: @scammya

from .. import loader, utils
import platform
import psutil

__version__ = (1, 0, 0)


def bytes_to_megabytes(b: int) -> int:
    return round(b / 1024 / 1024, 1)


@loader.tds
class SysInfoMod(loader.Module):
    """Simple System Info for Netfoll UserBot (And Hikka Support)"""

    strings = {
        "name": "SysInfo",
        "names": "☠️Info of System",
        "cpu": "☠️ CPU",
        "core": "Cores",
        "ram": "☠️ RAM",
        "use": "☠️ TrollUB Usage",
        "pyver": "☠️ Python",
        "release": "☠️ Release",
        "system": "☠️ OS",
    }

    strings_ru = {
        "names": "☠️ Информация о системе",
        "core": "Ядер",
        "use": "☠️ TrollUb Использует",
        "release": "☠️ Релиз ОС",
    }

    strings_uk = {
        "names": "☠️ Інформація про систему",
        "core": "Ядер",
        "use": "☠️  TrollUB використовує",
        "release": "☠️ Реліз ОС",
    }

    async def client_ready(self):
        if "Termux" in utils.get_named_platform():
            raise loader.SelfUnload

    def info(self, message):
        names = self.strings("names")
        processor = utils.escape_html(platform.architecture()[0])
        ram = bytes_to_megabytes(
            psutil.virtual_memory().total - psutil.virtual_memory().available
        )
        ram_load_mb = bytes_to_megabytes(psutil.virtual_memory().total)
        ram_load_procent = psutil.virtual_memory().percent

        return (
            f"<b>{names}</b>\n\n"
            f'<b>{self.strings("cpu")} ({processor}): {psutil.cpu_count(logical=True)} {self.strings("core")} ({psutil.cpu_percent()}%)</b>\n'
            f'<b>{self.strings("ram")}: {ram}/{ram_load_mb} MB ({ram_load_procent}%)</b>\n'
            f'<b>{self.strings("use")}: {utils.get_ram_usage()} MB / CPU {utils.get_cpu_usage()}%</b>\n\n'
            f'<b>{self.strings("pyver")}: {platform.python_version()}</b>\n'
            f'<b>{self.strings("release")}: {platform.version()}</b>\n'
            f'<b>{self.strings("system")}: {platform.system()} ({platform.release()})</b>\n\n'
        )

    @loader.command(ru_doc="Показать информацию о ☠️TrollHost")
    async def thinfocmd(self, message):
        """Show System"""
        await utils.answer(message, self.info(message))
