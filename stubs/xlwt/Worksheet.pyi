# Stubs for xlwt.Worksheet (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from .Style import XFStyle

class Worksheet:
    active_pane: int = ...
    Row: Any = ...
    Column: Any = ...
    show_zero_values: int = ...
    explicit_magn_setting: bool = ...
    visibility: int = ...
    split_position_units_are_twips: bool = ...
    row_default_height_mismatch: int = ...
    row_default_hidden: int = ...
    row_default_space_above: int = ...
    row_default_space_below: int = ...
    last_used_row: int = ...
    first_used_row: int = ...
    last_used_col: int = ...
    first_used_col: int = ...
    row_tempfile: Any = ...
    def __init__(self, sheetname: str, parent_book: Any, cell_overwrite_ok: bool = ...) -> None: ...
    def set_name(self, value: str) -> None: ...
    def get_name(self): ...
    name: str = ...
    def get_parent(self): ...
    parent: Any = ...
    def get_rows(self): ...
    rows: Any = ...
    def get_cols(self): ...
    cols: Any = ...
    def get_merged_ranges(self): ...
    merged_ranges: Any = ...
    def get_bmp_rec(self): ...
    bmp_rec: Any = ...
    def set_show_formulas(self, value: Any) -> None: ...
    def get_show_formulas(self): ...
    show_formulas: Any = ...
    def set_show_grid(self, value: Any) -> None: ...
    def get_show_grid(self): ...
    show_grid: Any = ...
    def set_show_headers(self, value: Any) -> None: ...
    def get_show_headers(self): ...
    show_headers: Any = ...
    def set_panes_frozen(self, value: Any) -> None: ...
    def get_panes_frozen(self): ...
    panes_frozen: Any = ...
    def set_auto_colour_grid(self, value: Any) -> None: ...
    def get_auto_colour_grid(self): ...
    auto_colour_grid: Any = ...
    def set_cols_right_to_left(self, value: Any) -> None: ...
    def get_cols_right_to_left(self): ...
    cols_right_to_left: Any = ...
    def set_show_outline(self, value: Any) -> None: ...
    def get_show_outline(self): ...
    show_outline: Any = ...
    def set_remove_splits(self, value: Any) -> None: ...
    def get_remove_splits(self): ...
    remove_splits: Any = ...
    def set_selected(self, value: Any) -> None: ...
    def get_selected(self): ...
    selected: Any = ...
    def set_sheet_visible(self, value: Any) -> None: ...
    def get_sheet_visible(self): ...
    sheet_visible: Any = ...
    def set_page_preview(self, value: Any) -> None: ...
    def get_page_preview(self): ...
    page_preview: Any = ...
    def set_first_visible_row(self, value: Any) -> None: ...
    def get_first_visible_row(self): ...
    first_visible_row: Any = ...
    def set_first_visible_col(self, value: Any) -> None: ...
    def get_first_visible_col(self): ...
    first_visible_col: Any = ...
    def set_grid_colour(self, value: Any) -> None: ...
    def get_grid_colour(self): ...
    grid_colour: Any = ...
    def set_preview_magn(self, value: Any) -> None: ...
    def get_preview_magn(self): ...
    preview_magn: Any = ...
    def set_normal_magn(self, value: Any) -> None: ...
    def get_normal_magn(self): ...
    normal_magn: Any = ...
    def set_scl_magn(self, value: Any) -> None: ...
    def get_scl_magn(self): ...
    scl_magn: Any = ...
    def set_vert_split_pos(self, value: Any) -> None: ...
    def get_vert_split_pos(self): ...
    vert_split_pos: Any = ...
    def set_horz_split_pos(self, value: Any) -> None: ...
    def get_horz_split_pos(self): ...
    horz_split_pos: Any = ...
    def set_vert_split_first_visible(self, value: Any) -> None: ...
    def get_vert_split_first_visible(self): ...
    vert_split_first_visible: Any = ...
    def set_horz_split_first_visible(self, value: Any) -> None: ...
    def get_horz_split_first_visible(self): ...
    horz_split_first_visible: Any = ...
    def set_show_auto_page_breaks(self, value: Any) -> None: ...
    def get_show_auto_page_breaks(self): ...
    show_auto_page_breaks: Any = ...
    def set_dialogue_sheet(self, value: Any) -> None: ...
    def get_dialogue_sheet(self): ...
    dialogue_sheet: Any = ...
    def set_auto_style_outline(self, value: Any) -> None: ...
    def get_auto_style_outline(self): ...
    auto_style_outline: Any = ...
    def set_outline_below(self, value: Any) -> None: ...
    def get_outline_below(self): ...
    outline_below: Any = ...
    def set_outline_right(self, value: Any) -> None: ...
    def get_outline_right(self): ...
    outline_right: Any = ...
    def set_fit_num_pages(self, value: Any) -> None: ...
    def get_fit_num_pages(self): ...
    fit_num_pages: Any = ...
    def set_show_row_outline(self, value: Any) -> None: ...
    def get_show_row_outline(self): ...
    show_row_outline: Any = ...
    def set_show_col_outline(self, value: Any) -> None: ...
    def get_show_col_outline(self): ...
    show_col_outline: Any = ...
    def set_alt_expr_eval(self, value: Any) -> None: ...
    def get_alt_expr_eval(self): ...
    alt_expr_eval: Any = ...
    def set_alt_formula_entries(self, value: Any) -> None: ...
    def get_alt_formula_entries(self): ...
    alt_formula_entries: Any = ...
    def set_row_default_height(self, value: Any) -> None: ...
    def get_row_default_height(self): ...
    row_default_height: Any = ...
    def set_col_default_width(self, value: Any) -> None: ...
    def get_col_default_width(self): ...
    col_default_width: Any = ...
    def set_calc_mode(self, value: Any) -> None: ...
    def get_calc_mode(self): ...
    calc_mode: Any = ...
    def set_calc_count(self, value: Any) -> None: ...
    def get_calc_count(self): ...
    calc_count: Any = ...
    def set_RC_ref_mode(self, value: Any) -> None: ...
    def get_RC_ref_mode(self): ...
    RC_ref_mode: Any = ...
    def set_iterations_on(self, value: Any) -> None: ...
    def get_iterations_on(self): ...
    iterations_on: Any = ...
    def set_delta(self, value: Any) -> None: ...
    def get_delta(self): ...
    delta: Any = ...
    def set_save_recalc(self, value: Any) -> None: ...
    def get_save_recalc(self): ...
    save_recalc: Any = ...
    def set_print_headers(self, value: Any) -> None: ...
    def get_print_headers(self): ...
    print_headers: Any = ...
    def set_print_grid(self, value: Any) -> None: ...
    def get_print_grid(self): ...
    print_grid: Any = ...
    def set_vert_page_breaks(self, value: Any) -> None: ...
    def get_vert_page_breaks(self): ...
    vert_page_breaks: Any = ...
    def set_horz_page_breaks(self, value: Any) -> None: ...
    def get_horz_page_breaks(self): ...
    horz_page_breaks: Any = ...
    def set_header_str(self, value: Any) -> None: ...
    def get_header_str(self): ...
    header_str: Any = ...
    def set_footer_str(self, value: Any) -> None: ...
    def get_footer_str(self): ...
    footer_str: Any = ...
    def set_print_centered_vert(self, value: Any) -> None: ...
    def get_print_centered_vert(self): ...
    print_centered_vert: Any = ...
    def set_print_centered_horz(self, value: Any) -> None: ...
    def get_print_centered_horz(self): ...
    print_centered_horz: Any = ...
    def set_left_margin(self, value: Any) -> None: ...
    def get_left_margin(self): ...
    left_margin: Any = ...
    def set_right_margin(self, value: Any) -> None: ...
    def get_right_margin(self): ...
    right_margin: Any = ...
    def set_top_margin(self, value: Any) -> None: ...
    def get_top_margin(self): ...
    top_margin: Any = ...
    def set_bottom_margin(self, value: Any) -> None: ...
    def get_bottom_margin(self): ...
    bottom_margin: Any = ...
    def set_paper_size_code(self, value: Any) -> None: ...
    def get_paper_size_code(self): ...
    paper_size_code: Any = ...
    def set_print_scaling(self, value: Any) -> None: ...
    def get_print_scaling(self): ...
    print_scaling: Any = ...
    def set_start_page_number(self, value: Any) -> None: ...
    def get_start_page_number(self): ...
    start_page_number: Any = ...
    def set_fit_width_to_pages(self, value: Any) -> None: ...
    def get_fit_width_to_pages(self): ...
    fit_width_to_pages: Any = ...
    def set_fit_height_to_pages(self, value: Any) -> None: ...
    def get_fit_height_to_pages(self): ...
    fit_height_to_pages: Any = ...
    def set_print_in_rows(self, value: Any) -> None: ...
    def get_print_in_rows(self): ...
    print_in_rows: Any = ...
    def set_portrait(self, value: Any) -> None: ...
    def get_portrait(self): ...
    portrait: Any = ...
    def set_print_colour(self, value: Any) -> None: ...
    def get_print_colour(self): ...
    print_colour: Any = ...
    def set_print_draft(self, value: Any) -> None: ...
    def get_print_draft(self): ...
    print_draft: Any = ...
    def set_print_notes(self, value: Any) -> None: ...
    def get_print_notes(self): ...
    print_notes: Any = ...
    def set_print_notes_at_end(self, value: Any) -> None: ...
    def get_print_notes_at_end(self): ...
    print_notes_at_end: Any = ...
    def set_print_omit_errors(self, value: Any) -> None: ...
    def get_print_omit_errors(self): ...
    print_omit_errors: Any = ...
    def set_print_hres(self, value: Any) -> None: ...
    def get_print_hres(self): ...
    print_hres: Any = ...
    def set_print_vres(self, value: Any) -> None: ...
    def get_print_vres(self): ...
    print_vres: Any = ...
    def set_header_margin(self, value: Any) -> None: ...
    def get_header_margin(self): ...
    header_margin: Any = ...
    def set_footer_margin(self, value: Any) -> None: ...
    def get_footer_margin(self): ...
    footer_margin: Any = ...
    def set_copies_num(self, value: Any) -> None: ...
    def get_copies_num(self): ...
    copies_num: Any = ...
    def set_wnd_protect(self, value: Any) -> None: ...
    def get_wnd_protect(self): ...
    wnd_protect: Any = ...
    def set_obj_protect(self, value: Any) -> None: ...
    def get_obj_protect(self): ...
    obj_protect: Any = ...
    def set_protect(self, value: Any) -> None: ...
    def get_protect(self): ...
    protect: Any = ...
    def set_scen_protect(self, value: Any) -> None: ...
    def get_scen_protect(self): ...
    scen_protect: Any = ...
    def set_password(self, value: Any) -> None: ...
    def get_password(self): ...
    password: Any = ...
    def write(self, r: int, c: int, label: str = ..., style: XFStyle = ...) -> None: ...
    def write_rich_text(self, r: Any, c: Any, rich_text_list: Any, style: Any = ...) -> None: ...
    def merge(self, r1: Any, r2: Any, c1: Any, c2: Any, style: Any = ...) -> None: ...
    def write_merge(self, r1: Any, r2: Any, c1: Any, c2: Any, label: str = ..., style: Any = ...) -> None: ...
    def insert_bitmap(self, filename: Any, row: Any, col: Any, x: int = ..., y: int = ..., scale_x: int = ..., scale_y: int = ...) -> None: ...
    def insert_bitmap_data(self, data: Any, row: Any, col: Any, x: int = ..., y: int = ..., scale_x: int = ..., scale_y: int = ...) -> None: ...
    def col(self, indx: Any): ...
    def row(self, indx: Any): ...
    def row_height(self, row: Any): ...
    def col_width(self, col: Any): ...
    def get_biff_data(self): ...
    def flush_row_data(self) -> None: ...