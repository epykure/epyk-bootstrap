
from epyk.core.html.options import Options


class OptionsDt(Options):
  """

  """

  @property
  def date(self):
    """
    Description:
    ------------
    Returns the component's model current date, a moment object or null if not set.

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/#date
    """
    return self._config_get()

  @date.setter
  def date(self, dt):
    self._config(dt)

  @property
  def dayViewHeaderFormat(self):
    """
    Description:
    ------------
    Changes the heading of the datepicker when in "days" view.

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/#dayviewheaderformat
    """
    return self._config_get('MMMM YYYY')

  @dayViewHeaderFormat.setter
  def dayViewHeaderFormat(self, dt):
    self._config(dt)

  @property
  def sideBySide(self):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/
    """
    return self._config_get(False)

  @sideBySide.setter
  def sideBySide(self, bool):
    self._config(bool)

  @property
  def inline(self):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/
    """
    return self._config_get(False)

  @inline.setter
  def inline(self, bool):
    self._config(bool)

  @property
  def daysOfWeekDisabled(self):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/
    """
    return self._config_get()

  @daysOfWeekDisabled.setter
  def daysOfWeekDisabled(self, bool):
    self._config(bool)

  @property
  def viewMode(self):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/
    """
    return self._config_get()

  @viewMode.setter
  def viewMode(self, bool):
    self._config(bool)

  @property
  def defaultDate(self):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/
    """
    return self._config_get(False)

  @defaultDate.setter
  def defaultDate(self, bool):
    self._config(bool)

  @property
  def format(self):
    """
    Description:
    ------------
    See momentjs' docs for valid formats. Format also dictates what components are shown, e.g. MM/dd/YYYY will not display the time picker.

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/#format
    """
    return self._config_get(False)

  @format.setter
  def format(self, bool):
    self._config(bool)

  @property
  def locale(self):
    """
    Description:
    ------------

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/
    """
    return self._config_get(False)

  @locale.setter
  def locale(self, bool):
    self._config(bool)

  @property
  def options(self):
    """
    Description:
    ------------
    Returns the components current options object.
    Note that the changing the values of the returned object does not change the components actual configuration. Use options(options) to set the components options massively or the other methods for setting config options individually.

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/#options_1
    """
    return self._report._jsStyles

  @options.setter
  def options(self, otps):
    if not otps is None:
      self._report._jsStyles.update(otps)

  @property
  def stepping(self):
    """
    Description:
    ------------
    Number of minutes the up/down arrow's will move the minutes value in the time picker

    Related Pages:

      https://eonasdan.github.io/bootstrap-datetimepicker/Options/#stepping
    """
    return self._config_get(1)

  @stepping.setter
  def stepping(self, num):
    self._config(num)

