"""Setting frame"""
from tkinter import INSERT

from gui.base_frame import BaseFrame
from utilities.db.tbl_setting import get_all_setting, update_setting


class SettingFrame(BaseFrame):
  """Setting frame"""
  def __init__(self, master):
    super().__init__(master, "Setting")

  def __init_frame__(self):
    super().__init_frame__()

    self.grid_columnconfigure(1, weight=1)

    self.add_label("AWS access key ID").grid(row=0, column=0)
    self.aws_access_key_id = self.add_entry()
    self.aws_access_key_id.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

    self.add_label("AWS secret access key").grid(row=1, column=0)
    self.aws_secret_access_key = self.add_entry()
    self.aws_secret_access_key.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

    save_btn = self.add_button("Save", self.save_setting)
    save_btn.grid(row=2, column=0, columnspan=2)

  def set_default_input(self):
    """default value for the input"""
    super().set_default_input()
    setting = get_all_setting()
    aws_access_key_id = setting.get("aws_access_key_id") if "aws_access_key_id" in setting else ""
    aws_secret_access_key = setting.get("aws_secret_access_key") if "aws_secret_access_key" in setting else ""
    self.aws_access_key_id.insert(INSERT, aws_access_key_id)
    self.aws_secret_access_key.insert(INSERT, aws_secret_access_key)

  def save_setting(self):
    """Save setting"""
    aws_access_key_id = self.aws_access_key_id.get()
    aws_secret_access_key = self.aws_secret_access_key.get()
    update_setting("aws_access_key_id", aws_access_key_id)
    update_setting("aws_secret_access_key", aws_secret_access_key)
