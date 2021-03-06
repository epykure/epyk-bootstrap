
from epyk.core import html
from epyk_bootstrap.core import BsDom


class BsComposite(html.HtmlTextComp.Composite):
  name = "Bootstrap Composite"

  extended_map = None

  @property
  def _get_comp_map(self):
    """
    Description:
    ------------
    This list is specific for the Bootstrap components.

    Span are replaced by div as I did not want to use the span as a container object.
    I believe this component should remain a base one.

    """

    if self.extended_map is None:
      self.extended_map = dict(super(BsComposite, self)._get_comp_map)
      self.extended_map.update({
        'close': self._report.bootstrap.buttons.close,
      })
    return self.extended_map


class Section(html.Html.Html):
  name = "Bootstrap Section"

  def __init__(self, report, type, data=None, options=None, profile=None):
    super(Section, self).__init__(report, [])
    self.style.clear_all()
    self.__section = type
    if data is not None:
      self.__add__(data)

  def __getitem__(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer. The internal row based on the index

    :rtype: Tr
    """
    return self.val[i]

  def __add__(self, component):
    """ Add items to a container """
    self.val.append(component)
    return self

  def insert(self, i, comp):
    """
    Description:
    ------------

    :param i:
    :param comp:
    """
    self.val.insert(i, comp)
    return self

  def __str__(self):
    cols = "".join([htmlObj.html() if hasattr(htmlObj, 'html') else str(htmlObj) for i, htmlObj in enumerate(self.val)])
    return '<%(section)s %(attr)s>%(cols)s</%(section)s>' % {'section': self.__section, 'cols': cols,
                  'attr': self.get_attrs(pyClassNames=self.style.get_classes())}


class BsToasts(html.Html.Html):
  name = "Bootstrap Toasts"

  def __init__(self, report, components, title, width, height, options, profile):
    super(BsToasts, self).__init__(report, [], profile=profile)
    self.style.clear_all()
    self.attr["class"].add("toast")
    self.attr["role"] = "alert"
    self.aria.live = "assertive"
    self.aria.atomic = True
    self.__body, self.__header = None, None
    for c in components:
      self.__add__(c)
    if title is not None:
      self.header.__add__(title)
    # $('.toast').toast('show')

  def __getitem__(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer. The internal row based on the index

    :rtype: Tr
    """
    if not self.body.val:
      return []

    return self.body.val[i]

  def __add__(self, comp):
    """
    Description:
    ------------
    Add items to a container

    :param comp:
    """
    self.body.__add__(comp)
    return self

  @property
  def header(self):
    """
    Description:
    ------------

    """
    if self.__header is None:
      self.__header = Section(self._report, 'div')
      self.__header.style.clear_all()
      self.__header.attr['class'].add('toast-header')
    return self.__header

  @property
  def body(self):
    """
    Description:
    ------------

    """
    if self.__body is None:
      self.__body = Section(self._report, 'div')
      self.__body.style.clear_all()
      self.__body.attr['class'].add('toast-body')
    return self.__body

  def __str__(self):
    return '<div %s>%s%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.header.html(), self.body.html())


class BsCards(html.Html.Html):
  name = "Bootstrap Card"

  def __init__(self, report, components, title, width, height, options, profile):
    super(BsCards, self).__init__(report, [], profile=profile)
    self.style.clear_all()
    self.__body, self.__header = None, None
    for c in components:
      self.__add__(c)
    if title is not None:
      self.header.__add__(title)

  def __getitem__(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer. The internal row based on the index

    :rtype: Tr
    """
    if not self.body.val:
      return []

    return self.body.val[i]

  def __add__(self, comp):
    """
    Description:
    ------------
    Add items to a container

    :param comp:
    """
    self.body.__add__(comp)
    return self

  def insert(self, i, comp):
    """
    Description:
    ------------

    :param i:
    :param comp:
    """
    self.body.insert(i, comp)
    return self

  @property
  def header(self):
    """
    Description:
    ------------

    """
    if self.__header is None:
      self.__header = Section(self._report, 'div')
      self.__header.style.clear_all()
      self.__header.attr['class'].add('card-header')
    return self.__header

  @property
  def body(self):
    """
    Description:
    ------------

    """
    if self.__body is None:
      self.__body = Section(self._report, 'div')
      self.__body.style.clear_all()
      self.__body.attr['class'].add('card-body')
    return self.__body

  def __str__(self):
    return '<div %s>%s%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.header.html(), self.body.html())


class BsModals(html.Html.Html):
  name = "Bootstrap Modals"
  
  def __init__(self, report, components, title, width, height, options, profile):
    super(BsModals, self).__init__(report, [])
    self.style.clear_all()
    self.attr['class'].add("modal fade")
    self.attr['role'] = 'dialog'
    self.attr['tabindex'] = -1
    self.aria.hidden = True
    self.aria.labelledby = ""
    self.dialog = Section(self._report, 'div')
    self.dialog.attr["class"].add('modal-dialog')
    self.dialog.attr["role"] = 'document'
    if options.get("vertical-align") == 'middle':
      self.dialog.attr["class"].add('modal-dialog-centered')
    self.dialog += Section(self._report, 'div')
    self._content = self.dialog[0]
    self._content.attr["class"].add('modal-content')
    header = Section(self._report, 'div')
    header.attr['class'].add('modal-header')
    body = Section(self._report, 'div')
    body.attr['class'].add('modal-body')
    footer = Section(self._report, 'div')
    footer.attr['class'].add('modal-footer')
    self._content += header
    self._content += body
    self._content += footer


    if title is not None:
      self.header.__add__(title)

    for c in components:
      self.body.__add__(c)

  def __add__(self, comp):
    """
    Description:
    ------------
    Add items to a container

    :param comp:
    """
    if hasattr(comp, 'options'):
      comp.options.managed = False
    self.body.__add__(comp)
    return self

  def __getitem__(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer. The internal row based on the index

    :rtype: Tr
    """
    if not self.body.val:
      return []

    return self.body.val[i]

  @property
  def dom(self):
    """
    Description:
    ------------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlPanels.JsHtmlPanel
    """
    if self._dom is None:
      self._dom = BsDom.Modal(self, report=self._report)
    return self._dom

  @property
  def header(self):
    return self._content[0]

  @property
  def body(self):
    return self._content[1]

  @property
  def footer(self):
    return self._content[2]

  def __str__(self):
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.dialog.html())
