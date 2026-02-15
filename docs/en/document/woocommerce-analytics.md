---
title: Analytics and Sales Reports
url: https://woocommerce.com/document/woocommerce-analytics/
---

The Analytics and Sales Reports offer nine reports along with advanced filtering and segmenting tools, the ability to download data to CSV, and a customizable dashboard to monitor key metrics of your store.

Since there is a great deal of functionality in the Analytics and Sales Reports, you can refer to the Table of Contents in the right sidebar of this page to quickly find information you’re looking for.

Most of the reports in the Analytics section have a set of common tools. This document will introduce you to those tools, and how they can be utilized to customize and dive deeper into the various analytics reports.

The table below describes how different metrics are calculated.

Refunds in the Analytics and Sales Reports are reported differently compared with the [legacy WooCommerce Reports](https://woocommerce.com/document/reports/).

In the Analytics and Sales Reports:

- Refunds appear as a negative number on the date that the return occurred (not the date the order was placed).
- Refunds include discounts from coupons.
- Refunded shipping charges and refunded taxes are not included in the Refunds summary number or columns. They appear as negative values in the shipping and taxes summary numbers and columns respectively.

**Note:** What is the difference between a refund and a return?

A **refund** encompasses the total amount that’s refunded to the customer which includes the value of goods or services purchased, shipping, and tax. A **return** only accounts for the value of goods or services in a refund, shipping and tax are tracked separately.

The **Date Range** picker allows you to specify which dates to include in the report being viewed. When you first open the Date Range Picker, a variety of popular presets allow you to quickly choose from common date ranges:

- Today
- Yesterday
- Week to Date
- Last Week
- Month to Date
- Last Month
- Quarter to Date
- Last Year

You can also select which date range to compare against, either the same range from the **Previous period** or **Previous year**.

If the presets don’t match your desired date range, select the “Custom” tab at the top of the picker for more granular control over the date range. In the custom picker, you can either manually enter the start and end date using the provided input fields, or use the calendar to make your selection.

After either choosing a preset, or a custom date range, use the **Update** button to modify the data in the report. By doing this, the date range selected is added to the address of the report URL, allowing you to bookmark or share a report URL with a specific date range with other Store admins. This date selection persists on the report view until you navigate away from the report.

Depending on the report you are viewing, there might also be other **Quick Filters** and/or **Advanced Filters** that allow you to further customize the data set being viewed.

If filter options are available, they will be shown next to the Date Range picker, or below it on narrow/mobile viewports. Much like the date range selection, filters are also added to the URL which allows you to save a quick link to a specific filtered version of a report. Available filters for each report are covered more in-depth in the documentation for each report.

From WooCommerce 10.5, Analytics now includes a Data Status Indicator and a manual ‘Update Now’ button to show when analytics data was last updated. This allows you to trigger imports on demand.

At the top of the report screen, the Summary number tabs and the corresponding chart offer quick access to key data, trends of that data, and visualizations for changes over time in the period selected, and the period being compared against.

#### Summary Numbers

The **Summary Number** tabs give you a quick view of the total figure for that metric over the period selected, the total number for the period being compared, and the percentage trend between those two figures. Select one of the **Summary Number** tabs to view that particular metric in the chart.

#### Chart

The charts on report screens offer quite a few options to customize the visualization of data. First, the **Data Legend** checkboxes allow you to toggle the visibility of different data set periods. For example, the selected range and the range to compare against. Next, the **Interval Selector** allows you to adjust the interval displayed in the chart such as by day, week, month, or quarter. The options available in the Interval selector are dependent upon the length of the date range selected. And lastly, you can adjust the **Type of Chart** being displayed, either a line or bar chart.

The table which displays the detailed data on Analytics reports also has a number of features that allow you to customize how the data is displayed, and an option to download a CSV copy of the data used in the report for further analysis.

#### Table Column Sorting

Many columns in reports will allow you to use the column header to sort the tabular data by that value and to either sort by that value in ascending or descending order. Simply select the column header to sort by that value, and click it again to change between ascending and descending sort.

#### Toggle Column Visibility

If a report contains a data column that you don’t need to be displayed, you can adjust the visibility of it by using the visibility menu on the right side of the table header. Toggle the column name in the menu to change the visibility of the column. Your visibility selections are persisted to your user preferences for each report, so on subsequent visits to that report, the columns you have previously disabled will not be displayed.

#### Download (to CSV)

If you would like to download a copy of the data contained in the report table, use the **Download** link upper right corner of the table header. If all the report data can be shown on a single screen, without pagination, the CSV file will download immediately. Otherwise, if your selected date range results in a data set that spans more than one page in the table, your CSV download will be processed as a background job by WooCommerce. Once the data is ready to be downloaded, an email will be sent to the address that is attached to your WordPress account with a link to download the file.

**Note:**

If you have more than one Admin on your site, the currently logged-in Admin who initiates the download will receive the report download email.

#### Table Pagination

When the data displayed in the table is larger than the default single page size of 25, pagination options will appear in the table footer area. You can move forward and backward through the pages using the directional arrow buttons or enter a number in the text field to jump to a specific page. Furthermore, you can change the number of rows to display per page.

#### Table Search Box

Some reports also provide a search box to filter and compare data. For details on what the search box does on a given report, please refer to the report’s documentation.

The Analytics and Sales Reports overview in WooCommerce has been designed to allow you to keep track of the statistics and data that matter most to your site. Each section of the dashboard can be fully customized to meet the needs of your store, and also act as launching points to dive deeper into other reports.

The dashboard on **WooCommerce > Overview** is comprised of three sections:

- Performance
- Charts
- Leaderboards

The data presented in these sections are controlled by the Date Picker at the top of the page. This lets you quickly look at data for a number of preset date-ranges like week, month, quarter, and year to date, or to select a specific date range to view.

These sections can be re-ordered, re-named, or even disabled if you don’t want to view a particular section.

To customize dashboard sections, use the customization menu (three vertical dots) in the top right corner of the section title. The first item that appears in this menu is the ability to toggle the display of the various stats that are shown in the section.

Below that you will find options for renaming the section, moving it up or down, or removing it entirely from the dashboard.

If you removed a dashboard section, or you have an extension installed that adds in an option for a new section, a plus icon will appear at the bottom of your dashboard. Selecting the plus icon will allow you to insert previously removed sections, or add in new ones.

By default, the Performance section appears at the top of your dashboard below the Date Picker. Each performance indicator includes the statistic label, the value of that statistic for the date range selected, and a color-coded percentage change over the prior period.

Beyond giving you a quick glimpse into the statistic, Performance Indicators also act as a quick shortcut to dive deeper into the data behind the stat. For example, selecting the Total Sales indicator will open the Revenue Report for the date range selected on the Dashboard. From there you can view associated charts and tabular data for deeper analysis.

You can toggle the display of the following default stats using the customization menu in the upper right corner of the section:

The next section displayed by default is Charts. The customization menu again allows you to toggle the display of charts that are most useful for your Store. The following charts are available to display in this section:

The charts section has a setting that allows you to set the time interval to display in the charts. The options displayed in the interval drop down are determined by how long of a date range you currently have selected in the Date Picker.

The last way you can customize the appearance of the charts is the ability to toggle between Line and Bar charts. Your selection chosen here will be saved to your user options and used on subsequent visits to the WooCommerce Dashboard.

The final section on the Dashboard allows you to view four different “Leaderboards” for your store’s statistics. Like the other two sections, you can also toggle the visibility of the leaderboards via the customization menu. By default you have the following four Leaderboards to choose from:

- Top Customers, Total Spend
- Top Coupons, Number of Orders
- Top Categories, Items Sold
- Top Products, Items Sold

WooCommerce is pre-configured with default settings for the Analytics and Sales Reports.

Navigate to **Analytics > Settings** to change the default settings.

In this section, order with these statuses that are **unchecked** are **included** from the totals in your analytics reports. **Checked** statuses are **excluded**. The Refunded status cannot be excluded. If your store uses custom order statuses, those statuses are included in the reports by default. They will be listed in this section under Custom Statuses and can be excluded via the status checkbox.

By default, Pending payment, Cancelled and Failed order statuses are excluded while Processing, On hold, and Completed order statuses are included.

Orders with these statuses require action on behalf of the store admin. These orders will be displayed in the Orders section of the [WooCommerce Home Screen](https://woocommerce.com/document/home-screen/#section-6).

The default date range is **Month to Date**. This setting will be used as the date range when loading the Analytics and Sales Reports Dashboard or Analytics page from any non-WooCommerce page. Any reports that support a date range will have a Date Range Picker to set the date range for the report.

Select the date field that should be considered for Revenue and Order Reports such as Date created, Date paid, or Date completed. The default date type is “Date Paid.”

WooCommerce 10.5 introduces a Update setting that controls how scheduled analytics imports are processed.

- **Scheduled**: Automatically updates analytics data every 12 hours. This option has the lowest performance impact and is recommended for most stores.
- **Immediately**: Updates analytics data as soon as new data becomes available. This may impact performance on high-traffic or busy stores.

The **“**Reset Defaults**“** button resets the settings to default values for all of the settings above the button. It has no effect on the data imported via **Import Historical Data**.

By default, a new store will not have historical data to import. However, if your store has Customer and Order data prior to the new Analytics and Sales Reports feature, you may want to import the data to ensure reports are accurate.

To start a historical data import, go to **Analytics > Settings**, and scroll down to **Import Historical Data**.

If you only want to see report data from a certain date onward, you can choose a date period, otherwise “All” data will be imported.

Extremely large or high volume stores might choose to import data in smaller increments – perhaps each year or quarter separately. The “skip previously imported customers and orders” control allows for overlapping date ranges to be imported without unnecessary data processing.

Select “Start” when you’re ready for the import to begin. The import will run in the background so it’s safe to navigate away from this page without affecting the import. You can return to **Analytics > Settings** at any time to monitor import progress.

Once you’ve started an import, the number of imported customers and orders will be periodically updated on the **Analytics > Settings** screen. If you need to stop the import at any time, select “Stop Import.” Data already imported will not be affected.

Once the import is complete, the status will show a summary of the imported data. For example, “Historical data from October 4, 2019 onward imported.”

You’ll also have the option to run another import or to delete previously imported data. **Please note that deletion is for analytics data** **only**. This doesn’t delete your products, orders, customers, etc.

If you need to reset the Analytics reports after importing historical data, you can do so from this settings screen by selecting **Delete Previously Imported Data**. Once that data is deleted your reports won’t show any information and you’ll want to re-import historical data, say a new time frame, or wait on new orders and customers to come in.

**Note:**

For new store owners, you’ll need to import data before the “Delete Previously Imported Data” button will be available. To import existing historical data, disable “Skip previously imported customers and orders” then start the import. Once the existing data has been imported, it can be deleted with the “Delete Previously Imported Data” button.

You can access the individual reports directly from your site’s dashboard. Below you will find detailed instructions on how to access and use them:

- [Categories report](https://woocommerce.com/document/woocommerce-analytics/categories-report/)
- [Coupons report](https://woocommerce.com/document/woocommerce-analytics/coupons-report/)
- [Customers report](https://woocommerce.com/document/woocommerce-analytics/customers-report/)
- [Downloads report](https://woocommerce.com/document/woocommerce-analytics/downloads-report/)
- [Orders report](https://woocommerce.com/document/woocommerce-analytics/orders-report/)
- [Order attribution report](https://woocommerce.com/document/woocommerce-analytics/order-attribution-report/)
- [Products report](https://woocommerce.com/document/woocommerce-analytics/products-report/)
- [Variations report](https://woocommerce.com/document/woocommerce-analytics/variations-report/)
- [Revenue report](https://woocommerce.com/document/woocommerce-analytics/revenue-report/)
- [Stock report](https://woocommerce.com/document/woocommerce-analytics/stock-report/)
- [Taxes report](https://woocommerce.com/document/woocommerce-analytics/taxes-report/)

WooCommerce has to process a large amount of data to generate the reports detailed in this section. To avoid potential performance issues the data is cached in a usable format and regularly updated.

If you notice that the figures displayed in the reports differ from the actual figures on your website you can clear the cache by going to **WooCommerce > Status > Tools** and running the **Clear Analytics Cache** tool. If the figures still look off after clearing the cache, try [re-importing historical data](https://woocommerce.com/document/woocommerce-analytics/#analytics-settings__import-historical-data).

Do you still have questions and need assistance?

This documentation is about the free, [core WooCommerce plugin](https://wordpress.org/plugins/woocommerce/), for which support is provided in our [community forums on WordPress.org](https://wordpress.org/support/plugin/woocommerce). By searching this forum, you’ll often find that your question has been asked and answered before. If you haven’t created a WordPress.org account to use the forums, [here’s how](https://make.wordpress.org/contribute/join/).

- If you’re looking to **extend** the core functionality shown here, we recommend reviewing available extensions in the [WooCommerce Marketplace](https://woocommerce.com/products/).
- Need ongoing advanced support or a **customization** built for WooCommerce? Hire a [Woo Agency Partner](https://woocommerce.com/customizations/).
- Are you a **developer** building your own WooCommerce integration or extension? Check our [Developer Resources](https://developer.woocommerce.com/).

If you weren’t able to find the information you need, please use the feedback thumbs below to let us know.

